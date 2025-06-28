import os
import asyncio
import aiohttp
from tenacity import retry, wait_fixed, stop_after_attempt

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_API_URL = "https://api.x.ai/groq/completions" 
HEADERS = {
    "Authorization": f"Bearer {GROQ_API_KEY}",
    "Content-Type": "application/json"
}

# Async Groq API call with retries
@retry(wait=wait_fixed(2), stop=stop_after_attempt(3))
async def llm_call(prompt: str, agent_name: str) -> str:
    payload = {
        "model": "grok-1",
        "prompt": prompt,
        "max_tokens": 300,
        "temperature": 0.7
    }

    async with aiohttp.ClientSession() as session:
        async with session.post(GROQ_API_URL, json=payload, headers=HEADERS) as resp:
            if resp.status != 200:
                text = await resp.text()
                raise Exception(f"Groq API error {resp.status}: {text}")
            data = await resp.json()

            # Adjust this based on Groq API response format
            # Example assumed: {"completion": "...text..."}
            completion = data.get("completion") or data.get("choices", [{}])[0].get("text")
            if not completion:
                raise Exception("No completion found in Groq API response")
            return completion.strip()

# Async Message Bus for inter-agent communication
class AsyncMessageBus:
    def __init__(self):
        self._queues = {}

    def _get_queue(self, agent_name):
        if agent_name not in self._queues:
            self._queues[agent_name] = asyncio.Queue()
        return self._queues[agent_name]

    async def send(self, agent_name, message):
        await self._get_queue(agent_name).put(message)

    async def receive(self, agent_name):
        queue = self._get_queue(agent_name)
        try:
            message = await asyncio.wait_for(queue.get(), timeout=10)
            return message
        except asyncio.TimeoutError:
            print(f"[{agent_name}] Timeout waiting for message.")
            return None

# Base Agent class
class Agent:
    def __init__(self, name, bus):
        self.name = name
        self.bus = bus

    async def run(self, *args, **kwargs):
        raise NotImplementedError

# Planner Agent
class PlannerAgent(Agent):
    async def run(self, user_query):
        prompt = f"You are the {self.name} agent. Plan how to answer this question:\n{user_query}"
        plan = await llm_call(prompt, self.name)
        await self.bus.send("Summarizer", plan)
        print(f"[Planner] Sent plan to Summarizer:\n{plan}\n")

# Summarizer Agent
class SummarizerAgent(Agent):
    async def run(self):
        plan = await self.bus.receive(self.name)
        if not plan:
            print("[Summarizer] No plan received, aborting.")
            return
        prompt = f"You are the {self.name} agent. Summarize the following plan:\n{plan}"
        summary = await llm_call(prompt, self.name)
        await self.bus.send("Answerer", summary)
        print(f"[Summarizer] Sent summary to Answerer:\n{summary}\n")

# Answerer Agent
class AnswererAgent(Agent):
    async def run(self, user_query):
        summary = await self.bus.receive(self.name)
        if not summary:
            print("[Answerer] No summary received, aborting.")
            return
        prompt = f"You are the {self.name} agent. Using this summary:\n{summary}\nAnswer the question:\n{user_query}"
        answer = await llm_call(prompt, self.name)
        print(f"[Answerer] Final answer:\n{answer}\n")

# Orchestrator
async def multi_agent_system(user_query):
    bus = AsyncMessageBus()
    planner = PlannerAgent("Planner", bus)
    summarizer = SummarizerAgent("Summarizer", bus)
    answerer = AnswererAgent("Answerer", bus)

    await planner.run(user_query)
    await summarizer.run()
    await answerer.run(user_query)

if __name__ == "__main__":
    question = "Explain what a multi-agent system is."
    asyncio.run(multi_agent_system(question))
