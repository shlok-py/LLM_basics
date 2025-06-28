# Multi-Agent Async Groq API System

This project demonstrates a simple multi-agent system implemented in Python using asynchronous programming with `asyncio` and `aiohttp`. It interacts with the Groq AI API (`https://api.x.ai/groq/completions`) to process natural language queries through a pipeline of agents:

- **PlannerAgent**: Plans how to answer a user query.
- **SummarizerAgent**: Summarizes the plan produced by the planner.
- **AnswererAgent**: Generates the final answer based on the summarized plan.

An asynchronous message bus coordinates communication between agents.

---

## Features

- Asynchronous communication between multiple agents via an internal message bus.
- Automatic retries with exponential backoff on API call failures (using `tenacity`).
- Modular agent design for easy extension.
- Uses Groq API for LLM completions.
- Timeout handling on message receipt.

---

## Requirements

- Python 3.8+
- `aiohttp`
- `tenacity`

Install dependencies using:

```bash
pip install aiohttp tenacity
```
## Environment Setup
Set your Groq API key as an environment variable before running:
```
export GROQ_API_KEY="your_groq_api_key_here"
```
## Usage
Run the script directly with Python:
```
python main.py
```
## How it Works

- The **PlannerAgent** receives the user query and generates a plan.  
- The **SummarizerAgent** receives the plan, summarizes it, and sends it onward.  
- The **AnswererAgent** receives the summary and produces the final answer.  
- Each agent communicates asynchronously via the `AsyncMessageBus`.

## Error Handling

- The LLM call uses retries with a fixed wait of 2 seconds, up to 3 attempts.  
- If any agent times out waiting for a message, it logs a timeout and aborts gracefully.

## Extending the System

- Add new agents by subclassing `Agent` and implementing `run`.  
- Enhance prompts or add prompt templates.  
- Integrate with other LLM APIs by replacing `llm_call`.
