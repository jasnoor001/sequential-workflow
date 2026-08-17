# sequential-workflow using LangGraph




# AI Content Transformation Pipeline

An AI-powered text transformation pipeline built using **Python, LangGraph, LangChain, and Mistral AI**.
The workflow processes raw text through three sequential AI nodes.
**Editor Node** corrects grammar, spelling, and improves text flow.
**Script Writer Node** converts the edited content into an engaging video script.
**Translator Node** converts the script into natural **Hinglish**.
LangGraph manages the workflow using a shared `TypedDict` state.
The pipeline follows: **Raw Input → Editor → Script Writer → Translator → Final Output**.
Mistral AI is used as the underlying LLM for all processing stages.
This project demonstrates **LLM orchestration, state management, and sequential AI workflows**.
Future improvements can include conditional routing, human approval, memory, and additional AI agents.
