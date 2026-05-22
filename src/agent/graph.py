"""
graph.py
========
Compiles the PoolAgent LangGraph workflow.

Node topology
─────────────
                    ┌─────────────┐
         START ───► │   planner   │
                    └──────┬──────┘
                           │ Command(goto="orchestrator")
                    ┌──────▼──────┐ ◄─────────────────────┐
                    │ orchestrator│ Command(goto="orchestrator") (loop)
                    └──────┬──────┘
                           │ Command(goto="synthesizer")
                    ┌──────▼──────┐
                    │ synthesizer │
                    └──────┬──────┘
                           │
                          END

Routing notes
─────────────
• planner and orchestrator return `Command` objects, so their edges are declared
  with `add_node(..., destinations=[...])` rather than `add_edge` / `add_conditional_edges`.
• synthesizer returns a plain dict → simple edge to END.
• The orchestrator loops back to itself until all execution_plan steps are done,
  then routes to synthesizer.
"""

from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import InMemorySaver

from state import PoolAgentState
from nodes import planner, orchestrator, synthesizer     # Synthesizer node

# ================================================================
# BUILD GRAPH
# ================================================================

def build_graph(checkpointer=None):
    """
    Construct and compile the PoolAgent StateGraph.

    Args:
        checkpointer: Optional LangGraph checkpointer for persistence.
                      Defaults to InMemorySaver() for short-term memory.

    Returns:
        Compiled LangGraph application ready to invoke.
    """
    builder = StateGraph(PoolAgentState)

    # ── Register nodes ────────────────────────────────────────────────────────
    # Nodes that return Command must declare their possible destinations so
    # LangGraph can validate the graph at compile time.

    builder.add_node(
        "planner",
        planner,
        destinations=["orchestrator"],          # planner always goes to orchestrator
    )

    builder.add_node(
        "orchestrator",
        orchestrator,
        destinations=["orchestrator", "synthesizer"],   # loops or exits
    )

    builder.add_node("synthesizer", synthesizer)

    # ── Wire edges ────────────────────────────────────────────────────────────
    builder.add_edge(START, "planner")          # entry point
    builder.add_edge("synthesizer", END)        # terminal node

    # planner → orchestrator and orchestrator → orchestrator / synthesizer
    # are handled dynamically by the Command objects returned in each node,
    # no explicit add_edge needed for those transitions.

    # ── Compile ───────────────────────────────────────────────────────────────
    _checkpointer = checkpointer or InMemorySaver()

    app = builder.compile(checkpointer=_checkpointer)
    return app


# ================================================================
# DEFAULT EXPORT
# ================================================================

graph = build_graph()