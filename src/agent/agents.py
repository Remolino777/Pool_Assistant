"""
agents.py
=========
Defines the sub-agents used inside the orchestrator pipeline.

Currently implemented
─────────────────────
  • general      – General pool discussions and educational information.
  • out_of_scope – Polite refusal handler for topics outside the agent's scope.

Stub slots (wire up when ready)
────────────────────────────────
  • diagnosis   – Symptom → chemical parameter mapping.
  • dosage      – RAISES / LOWERS chemical dosage calculations.
  • equipment   – CORRODES / SCALES / DEGRADES hardware evaluations.
  • maintenance – Routine, seasonal, and calendar-based procedures.
"""

from langchain_core.tools import tool
from langchain.agents import create_agent
from langgraph_supervisor import create_supervisor

from state import AgentName
from src.config.llm import create_llm
from src.agent.prompts import (
    GENERAL_PROMPT,
    OOS_PROMPT,
    SUPERVISOR_PROMPT,
)
# ================================================================
# SHARED LLM
# ================================================================

llm = create_llm()

# ================================================================
# TOOLS
# ================================================================

@tool
def pool_general_knowledge(topic: str) -> str:
    """
    Retrieve general knowledge and best practices for a pool-related topic.

    Args:
        topic: The specific pool subject to look up
               (e.g. 'saltwater pools', 'water balance', 'pool covers').
    """
    # Replace with a real knowledge-base / RAG call when available.
    return (
        f"General pool information about '{topic}': "
        "Please provide a comprehensive, helpful explanation based on your training knowledge."
    )

# ================================================================
# SUB-AGENTS
# ================================================================

general_agent = create_agent(
    model=llm,
    tools=[pool_general_knowledge],
    name="general",
    system_prompt=GENERAL_PROMPT,
)

oos_agent = create_agent(
    model=llm,
    tools=[],
    name="out_of_scope",
    system_prompt=OOS_PROMPT,
)

# ── Stubs ────────────────────────────────────────────────────────────────────
# Uncomment and implement each agent as you build the specialist modules.
#
# from diagnosis_agent  import diagnosis_agent
# from dosage_agent     import dosage_agent
# from equipment_agent  import equipment_agent
# from maintenance_agent import maintenance_agent

# ================================================================
# SUPERVISOR WORKFLOW
# ================================================================

workflow= create_supervisor(
    agents=[general_agent, oos_agent],
    model=llm,
    prompt=SUPERVISOR_PROMPT
)

pool_supervisor = workflow.compile()

# ================================================================
# AGENT REGISTRY
# ================================================================

AGENT_REGISTRY: dict[str, object] = {
    "general":     general_agent,
    "ooo":         oos_agent,          # planner uses "ooo" as the OOS agent name
    # ── Plug in when ready ────────────────────────────────────────
    # "diagnosis":   diagnosis_agent,
    # "dosage":      dosage_agent,
    # "equipment":   equipment_agent,
    # "maintenance": maintenance_agent,
}


def get_agent_by_name(agent_name: AgentName):
    """
    Return the compiled agent graph for *agent_name*.
    Raises ValueError if the agent is not yet registered.
    """
    agent = AGENT_REGISTRY.get(agent_name)
    if agent is None:
        raise ValueError(
            f"Agent '{agent_name}' is not registered in the agent registry. "
            f"Available agents: {list(AGENT_REGISTRY.keys())}"
        )
    return agent