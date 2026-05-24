![image alt](https://github.com/Remolino777/Pool_Assistant/blob/3cd8d219aeb33de51a302c44da7a56c5df23a798/banner.png)
# Pool Chemistry & Maintenance AI Assistant 🏊‍♂️🤖

A multi-agent generative AI orchestrator built to diagnose, prescribe, and manage pool chemistry and hardware maintenance. This project leverages a **LangGraph** supervisor workflow, integrating a **Neo4j** knowledge graph and a **Qdrant** vector store for hybrid search retrieval, fully observable via **Langfuse** and systematically evaluated via **Giskard**.

## 🏗 Architecture & Core Concepts

This system breaks away from standard linear RAG by employing a robust **Multi-Agent Orchestration** pattern. 

The core pipeline operates on a Planner-Orchestrator-Synthesizer flow:
1. **Planner (`chains.py` & `nodes.py`):** Deconstructs complex user inputs into atomic tasks (e.g., separating a symptom diagnosis from a dosage calculation) using structured function calling. Identifies language (en/es).
2. **Supervisor Orchestrator (`agents.py`):** Routes atomic tasks to specialized sub-agents (`diagnosis`, `dosage`, `equipment`, `maintenance`, `general`, `ooo`).
3. **Tools & Retrieval (`tools.py`):** Sub-agents execute tools that query a Neo4j knowledge graph (via Cypher) and a local Qdrant Vector Store (Hybrid Search: Gemini dense embeddings + BM25 sparse).
4. **Synthesizer:** Merges the dual-track agent results into a cohesive, conversational response in the user's detected language.

### Tech Stack
* **Framework:** [LangChain](https://python.langchain.com/) / [LangGraph](https://python.langchain.com/docs/langgraph/)
* **LLMs:** Google Gemini (Gemini 3 Flash Preview, Gemini 2.5 Flash Lite)
* **Observability:** [Langfuse](https://langfuse.com/) (using `@observe` decorators)
* **Evaluation & CI/CD:** [Giskard](https://giskard.ai/) (Vulnerability scanning & RAG correctness)
* **Databases:** * [Neo4j Aura](https://neo4j.com/cloud/platform/aura-graph-database/) (Graph DB)
  * [Qdrant](https://qdrant.tech/) (Local Hybrid Vector Store)
* **Embeddings:** `gemini-embedding-001` (Dense) + `FastEmbedSparse` (Sparse)
* **Validation:** Pydantic (State management & Structured Outputs)
