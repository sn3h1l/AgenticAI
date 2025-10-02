


# AgenticAI Project

This repository contains Jupyter notebooks and Python scripts for agentic workflows using LangChain, LangGraph, OpenAI, and Gemini models:

## Notebooks
- **conditional_flow.ipynb**: Conditional logic workflows (add/subtract, etc.)
- **parallel_flow_llm.ipynb**: Parallel execution using LLMs (OpenAI/Gemini)
- **parallel_flow_wo_llms.ipynb**: Parallel flows for cricket stats (no LLM)
- **prompt_chain.ipynb**: Blog generation via prompt chaining
- **chatbot.ipynb**: Agentic chatbot with custom logic
- **persistance.ipynb**: Demonstrates state persistence and checkpointing in agentic flows using Gemini and LangGraph.
- **iterative_flow.ipynb**: Shows iterative logic and state updates in agentic workflows.

## Backend
- **chatbot_backend.py**: Implements the chatbot logic using LangChain, LangGraph, and Gemini (Google Generative AI). Defines a state graph for message handling and response generation. Can be run as a standalone bot or used as a backend for the frontend UI.

## Frontend
- **chatbot_frontend.py**: Streamlit-based UI for the chatbot. Imports the backend workflow, manages chat history, and displays user/assistant messages interactively. Run with `streamlit run chatbot_frontend.py` for a web interface.

## Advanced Chatbot Scripts
- **streaming_chatbot.py**: Streamlit UI for a chatbot with streaming responses. Uses workflow.stream to display bot replies in real time.
- **threaded_chatbot.py**: Streamlit UI supporting multiple chat threads. Allows starting new threads and manages chat history per thread.

**.env**: Add your API keys here
