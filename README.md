



# AgenticAI Project

This repository contains Jupyter notebooks and Python scripts for agentic workflows using LangChain, LangGraph, OpenAI, and Gemini models:

## Notebooks
- **conditional_flow.ipynb**: Conditional logic workflows (add/subtract, etc.)
- **parallel_flow_llm.ipynb**: Parallel execution using LLMs (OpenAI/Gemini)
- **parallel_flow_wo_llms.ipynb**: Parallel flows for cricket stats (no LLM)
- **prompt_chain.ipynb**: Blog generation via prompt chaining
- **chatbot.ipynb**: Agentic chatbot with custom logic
- **persistance.ipynb**: State persistence and checkpointing in agentic flows (Gemini, LangGraph)
- **iterative_flow.ipynb**: Iterative logic and state updates in agentic workflows

## Backend
- **chatbot_backend.py**: Chatbot logic using LangChain, LangGraph, and Gemini. Defines a state graph for message handling and response generation. Usable standalone or as backend for UI.

## Frontend
- **chatbot_frontend.py**: Streamlit UI for the chatbot. Imports backend workflow, manages chat history, and displays user/assistant messages. Run with `streamlit run chatbot_frontend.py`.

## Advanced Chatbot Scripts
- **streaming_chatbot.py**: Streamlit UI for chatbot with streaming responses. Displays bot replies in real time using workflow.stream.
- **threaded_chatbot.py**: Streamlit UI supporting multiple chat threads. Allows starting new threads, manages chat history per thread, and provides a sidebar for thread control.

**.env**: Add your API keys here
