from langchain_core.messages import AIMessage, SystemMessage
from langgraph.types import Command
from langfuse import observe
from state import PoolAgentState
from prompts import PLANNER_PROMPT
from chains import create_planner_chain
from config import create_llm

# ================================================================
# CONFIGURATION
# ================================================================
llm = create_llm()
planner_chain = create_planner_chain(llm)  # Initialize the planner chain

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

# =====================================================================
# ORCHESTRATOR NODE
# =====================================================================
@observe(as_type='trace', name="Orchestrator Node")
def orchestrator(state: PoolAgentState):
    """
    Placeholder for the orchestrator node that would execute the clinical tasks.
    """
    return {"messages": [SystemMessage(content="Orchestratornode reached. Ready to execute clinical tasks.")]}

# ─────────────────────────────────────────────