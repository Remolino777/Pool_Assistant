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
from langfuse import observe

from .state import AgentName
from src.config.llm import create_llm, create_routing_llm, create_synthesizer_llm
from src.agent.prompts import (
    GENERAL_PROMPT,
    OOS_PROMPT,
    SUPERVISOR_PROMPT,
    DIAGNOSIS_PROMPT,
    DOSAGE_PROMPT,
    EQUIPMENT_PROMPT,
    MAINTENANCE_PROMPT,
)
from .tools import (
        query_symptom_graph,
        search_troubleshooting_kb,
        query_chemical_actions,
        get_dosing_formulas,
        query_hardware_impact,
        query_hardware_impact,
        search_equipment_manuals,
        search_maintenance_procedures,
        query_maintenance_dependencies,
        calculate_lsi,
        interpret_lsi,
        recommend_lsi_correction,
        analyze_pool_lsi,
        )
# ================================================================
# SHARED LLM
# ================================================================

llm = create_llm()
routing_llm = create_routing_llm()
synthesizer_llm = create_synthesizer_llm()

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
    model=synthesizer_llm,
    tools=[pool_general_knowledge],
    name="general",
    system_prompt=GENERAL_PROMPT,
)

oos_agent = create_agent(
    model=synthesizer_llm,
    tools=[],
    name="out_of_scope",
    system_prompt=OOS_PROMPT,
)

diagnosis_agent = create_agent(
    model=llm,
    tools=[
        query_symptom_graph,
        search_troubleshooting_kb,
        ],
    name="diagnosis",
    system_prompt=DIAGNOSIS_PROMPT,
)

dosage_agent = create_agent(
    model=routing_llm,
    tools=[
        query_chemical_actions,
        get_dosing_formulas,
        ],
    name="dosage",
    system_prompt=DOSAGE_PROMPT,
)

equipment_agent = create_agent(
    model=llm,
    tools=[
        query_hardware_impact,
        search_equipment_manuals,
        ],
    name="equipment",
    system_prompt=EQUIPMENT_PROMPT,
)

maintenance_agent = create_agent(
    model=llm,
    tools=[
        search_maintenance_procedures,
        query_maintenance_dependencies,
        calculate_lsi,
        interpret_lsi,
        recommend_lsi_correction,
        analyze_pool_lsi,
        ],
    name="maintenance",
    system_prompt=MAINTENANCE_PROMPT,
)   



# ================================================================
# SUPERVISOR WORKFLOW
# ================================================================

workflow= create_supervisor(
    agents=[
        general_agent, 
        oos_agent,
        diagnosis_agent,
        dosage_agent,
        equipment_agent,
        maintenance_agent,
        ],
    model=routing_llm,
    prompt=SUPERVISOR_PROMPT
)

pool_supervisor = workflow.compile()

# ================================================================
# AGENT REGISTRY
# ================================================================

AGENT_REGISTRY: dict[str, object] = {
    "general":     general_agent,
    "ooo":         oos_agent,
    "diagnosis":   diagnosis_agent,
    "dosage":      dosage_agent,
    "equipment":   equipment_agent,
    "maintenance": maintenance_agent,
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