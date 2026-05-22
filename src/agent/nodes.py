from langchain_core.messages import AIMessage, SystemMessage, HumanMessage
from langgraph.types import Command
from langfuse import observe
from state import PoolAgentState, ExecutionStep, AgentResult
from prompts import PLANNER_PROMPT, SYNTHESIZER_PROMPT
from chains import create_planner_chain
from src.config.llm import create_llm
from agents import get_agent_by_name
# ================================================================
# CONFIGURATION
# ================================================================
llm = create_llm()
planner_chain = create_planner_chain(llm)  # Initialize the planner chain

# ================================================================
# HELPERS
# ================================================================
 
def _extract_text(content) -> str:
    """Normalise LLM content to plain text regardless of its shape."""
    if isinstance(content, list):
        return " ".join(
            item.get("text", "")
            for item in content
            if isinstance(item, dict) and item.get("text", "").strip()
        ).strip()
    return str(content).strip()
 
 
def _run_step(step: ExecutionStep, user_message: str) -> AgentResult:
    """
    Invoke the agent assigned to *step* and return an AgentResult.
 
    The agent receives:
      - The literal task description produced by the Planner.
      - The original user message as context.
    """
    agent = get_agent_by_name(step.assigned_agent)
 
    agent_input = {
        "messages": [
            HumanMessage(
                content=(
                    f"Task: {step.task}\n\n"
                    f"User context: {user_message}"
                )
            )
        ]
    }
 
    result = agent.invoke(agent_input)
 
    # Walk message list in reverse; grab the last real AI response
    output_text = ""
    for msg in reversed(result.get("messages", [])):
        if isinstance(msg, AIMessage) and msg.content:
            output_text = _extract_text(msg.content)
            break
 
    return AgentResult(
        agent=step.assigned_agent,
        step=step.step,
        output=output_text,
    )

_LANGUAGE_MAP: dict[str, str] = {
    "es": (
        "Spanish (Latin American). "
        "Every single word must be in Spanish. Translate anything that is not."
    ),
    "en": (
        "English. "
        "Every single word must be in English. Translate anything that is not."
    ),
}
 
_OOS_INSTRUCTION_ACTIVE = (
    "IMPORTANT — OUT OF SCOPE RESPONSE: The user's request falls outside your area of "
    "expertise as a Pool Assistant. Do NOT attempt to answer the question. Instead, "
    "acknowledge the topic briefly, explain politely that it is outside your scope, "
    "and invite the user to ask any pool or spa related question."
)
 
_OOS_INSTRUCTION_INACTIVE = (
    "Provide a complete, helpful, and technically accurate response based on the raw "
    "content supplied. Do not add disclaimers about scope; the content is fully on-topic."
)
 
 
def _is_oos(execution_plan: list[ExecutionStep]) -> bool:
    """Return True when the plan is a single OOS step."""
    return (
        len(execution_plan) == 1
        and execution_plan[0].oos
    )
 
 
def _build_raw_content(agent_results: dict[str, AgentResult]) -> str:
    """
    Concatenate the outputs from every completed step in sequential order.
    Steps with errors are surfaced so the synthesizer can acknowledge gaps.
    """
    if not agent_results:
        return ""
 
    # Sort by the embedded step number ("step_1", "step_2", …)
    sorted_results: list[AgentResult] = sorted(
        agent_results.values(),
        key=lambda r: r.step,
    )
 
    sections: list[str] = []
    for result in sorted_results:
        if result.error:
            sections.append(
                f"[Step {result.step} — {result.agent}] ERROR: {result.error}"
            )
        elif result.output:
            sections.append(
                f"[Step {result.step} — {result.agent}]\n{result.output}"
            )
 
    return "\n\n".join(sections)
 
# ================================================================
# PLANNER NODE  
# ================================================================

@observe(as_type='trace', name="Planner Node")
def planner(state: PoolAgentState):
    user_input = state["messages"][-1].content

    # ── Context: Use only the last visible agent message + current user input
    agent_messages = [
        m for m in state["messages"]
        if isinstance(m, AIMessage) and getattr(m, "name", None) == "PiscinaAgent"
    ]
    
    last_agent_msg = agent_messages[-1].content if agent_messages else ""
    if isinstance(last_agent_msg, list):
        last_agent_msg = " ".join(
            i.get("text", "") for i in last_agent_msg if isinstance(i, dict)
        ).strip()

    context_for_planner = (
        f"[Last agent message]: {last_agent_msg}\n"
        f"[User reply]: {user_input}"
        if last_agent_msg
        else user_input
    )

    # Invoke structured chain -> Generates an instance of PlannerOutput
    plan = planner_chain.invoke([
        {"role": "system", "content": PLANNER_PROMPT},
        {"role": "user",   "content": context_for_planner},
    ])

    # Priorizamos la última detección para permitir cambios de idioma fluidos
    detected_language = plan.detected_language or state.get("detected_language") or "es"

    # Always route to Orchestrator as requested
    goto_node = "orchestrator"

    return Command(
        update={
            "detected_language": detected_language,
            "execution_plan": plan.execution_plan,
        },
        goto=goto_node,
    )

# ================================================================
# ORCHESTRATOR NODE
# ================================================================
 
@observe(as_type="trace", name="Orchestrator Node")
def orchestrator(state: PoolAgentState) -> Command:
    """
    Iterates through the execution_plan produced by the Planner, executing one
    step per invocation.  When all steps are complete it routes to the Synthesizer.
 
    State fields consumed:
        execution_plan   – ordered list of ExecutionStep
        current_step     – 0-based index of the step to run next (default 0)
        messages         – conversation history (last user message used as context)
        agent_results    – accumulated results dict (mutated and returned)
 
    State fields produced:
        agent_results    – updated with the result of the current step
        current_step     – incremented by 1
    """
    execution_plan = state.get("execution_plan", [])
    agent_results  = dict(state.get("agent_results") or {})
    current_idx    = state.get("current_step", 0)
 
    # ── Guard: nothing to execute ──────────────────────────────────────────────
    if not execution_plan:
        return Command(
            update={"error": "execution_plan is empty; cannot orchestrate."},
            goto="synthesizer",
        )
 
    # ── Guard: all steps already processed ────────────────────────────────────
    if current_idx >= len(execution_plan):
        return Command(goto="synthesizer")
 
    # ── Identify the current step ──────────────────────────────────────────────
    step = execution_plan[current_idx]
    step_key = f"step_{step.step}"
 
    # ── Extract latest user message as context for the agent ──────────────────
    messages = state.get("messages", [])
    user_message = ""
    for msg in reversed(messages):
        if hasattr(msg, "type") and msg.type == "human":
            user_message = _extract_text(msg.content)
            break
 
    # ── Run the agent for this step ────────────────────────────────────────────
    try:
        agent_result = _run_step(step, user_message)
    except Exception as exc:
        agent_result = AgentResult(
            agent=step.assigned_agent,
            step=step.step,
            output="",
            error=str(exc),
        )
 
    agent_results[step_key] = agent_result
 
    # ── Decide next destination ────────────────────────────────────────────────
    next_idx = current_idx + 1
    goto = "orchestrator" if next_idx < len(execution_plan) else "synthesizer"
 
    return Command(
        update={
            "agent_results": agent_results,
            "current_step": next_idx,
        },
        goto=goto,
    )

# ================================================================
# SYNTHESIZER NODE
# ================================================================
 
@observe(as_type="generation", name="Synthesizer Node")
def synthesizer(state: PoolAgentState) -> dict:
    """
    Reads the accumulated agent_results from the orchestrator, formats them into
    a single cohesive prompt, and produces the final user-facing AIMessage.
 
    State fields consumed:
        agent_results     – Dict[str, AgentResult] from orchestrator steps
        execution_plan    – used for OOS detection
        detected_language – "es" | "en"  (defaults to "es")
 
    State fields produced:
        messages          – appends a single AIMessage(name="Izel")
    """
 
    # ── 1. Collect & validate inputs ──────────────────────────────────────────
    execution_plan: list[ExecutionStep] = state.get("execution_plan", [])
    agent_results:  dict[str, AgentResult] = state.get("agent_results") or {}
    language_code:  str = state.get("detected_language", "es")
 
    # ── 2. OOS detection ──────────────────────────────────────────────────────
    is_oos = _is_oos(execution_plan)
    oos_instruction = _OOS_INSTRUCTION_ACTIVE if is_oos else _OOS_INSTRUCTION_INACTIVE
 
    # ── 3. Language instruction ───────────────────────────────────────────────
    language_instruction = _LANGUAGE_MAP.get(language_code, _LANGUAGE_MAP["es"])
 
    # ── 4. Build raw_content from agent_results ───────────────────────────────
    raw_content = _build_raw_content(agent_results)
    if not raw_content:
        raw_content = "(no prior content — generate a warm greeting and offer help)"
 
    # ── 5. Format system prompt ───────────────────────────────────────────────
    system_content = SYNTHESIZER_PROMPT.format(
        oos_instruction=oos_instruction,
        language=language_instruction,
        raw_content=raw_content,
    )
 
    # ── 6. Invoke LLM ─────────────────────────────────────────────────────────
    response = llm.invoke([
        SystemMessage(content=system_content),
        HumanMessage(content="Generate the final refined response now."),
    ])
 
    # ── 7. Normalise response content ─────────────────────────────────────────
    content = response.content
    if isinstance(content, list):
        final_text = " ".join(
            item.get("text", "")
            for item in content
            if isinstance(item, dict) and item.get("text", "").strip()
        ).strip()
    else:
        final_text = str(content).strip()
 
    # ── 8. Return the clean AIMessage ─────────────────────────────────────────
    return {
        "messages": [AIMessage(content=final_text, name="Izel")]
    }
 