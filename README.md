# AgenticAI Project

This repository contains several Jupyter notebooks demonstrating agentic workflows using LangChain, LangGraph, and OpenAI models. Below is a summary of each file:

## Notebooks

### conditional_flow.ipynb
Demonstrates conditional logic in agentic workflows. Uses LangChain, LangGraph, and OpenAI to perform operations based on user-defined choices (addition, subtraction, etc.). Includes custom state management and function nodes.

### parallel_flow_llm.ipynb
Shows parallel execution of tasks using LLMs. Utilizes structured output from OpenAI models and demonstrates how to generate random numbers and manage state in parallel flows.

### parallel_flow_wo_llms.ipynb
Illustrates parallel flows without LLMs, focusing on cricket statistics calculations (strike rate, balls per boundary, summary) using custom Python functions and state management.

### prompt_chain.ipynb
Implements a prompt chaining workflow for blog generation. Uses LangChain and OpenAI to create a blog outline and then generate a full blog post based on that outline.

## Environment

### .env
Environment file for storing API keys and configuration variables. Currently empty; add your OpenAI or other API keys as needed.

---
For more details, open each notebook and review the code and comments. These examples are useful for learning agentic workflows, prompt chaining, and parallel execution with and without LLMs.
