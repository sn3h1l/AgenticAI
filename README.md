<!-- ...existing code... -->
# AgenticAI Project

Minimal overview of files in this repository:

Notebooks
- `chatbot.ipynb` — chatbot example using state graphs
- `conditional_flow.ipynb` — conditional agent flows
- `iterative_flow.ipynb` — iterative state updates and loops
- `tool_nodes.ipynb` — tool node examples: LLM tool invocation and ToolNode usage (search, calculator, stock price)
- `parallel_flow_llm.ipynb` — parallel flows with LLMs
- `parallel_flow_wo_llms.ipynb` — parallel flows without LLMs
- `persistance.ipynb` — checkpointing and persistence examples
- `prompt_chain.ipynb` — prompt chaining (blog generation)

Backend / scripts
- `chatbot_backend.py` — chatbot state graph and LLM integration (Gemini/OpenAI)
- `chatbot_backend_database.py` — backend integration with a database (SQLite)

Frontend / apps
- `chatbot_frontend.py` — simple Streamlit UI
- `streaming_chatbot.py` — Streamlit UI with streaming responses
- `threaded_chatbot.py` — Streamlit UI supporting multiple threads
- `threaded_sqlite_bot.py` — threaded chatbot using SQLite for persistence
- `langsmith_threadwise_bot.py` — Streamlit thread-based chatbot UI: lists threads, start/reset threads, loads thread history from chatbot_backend_database, and streams assistant responses
