import requests
import numpy as np
import re
import faiss
import os
from sentence_transformers import SentenceTransformer
from datasets import load_dataset
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq()

model = SentenceTransformer("all-MiniLM-L6-v2")

# Global store
vector_index = None
text_chunks = []

# --- Tavily Search ---
def search_tavily(query, site=None, num_results=5):
    url = "https://api.tavily.com/search"
    headers = {"Content-Type": "application/json"}
    if site:
        query = f"site:{site} {query}"
    payload = {
        "api_key": os.environ["TAVILY_API_KEY"],
        "query": query,
        "search_depth": "advanced",
        "include_answer": True,
        "include_raw_content": True,
        "max_results": num_results
    }
    res = requests.post(url, json=payload, headers=headers)
    return [r['content'] for r in res.json().get("results", [])]

# --- Chunking ---
def chunk_text(text, max_tokens=200):
    sentences = text.split(". ")
    chunks, chunk = [], ""
    for s in sentences:
        if len(chunk.split()) + len(s.split()) < max_tokens:
            chunk += s + ". "
        else:
            chunks.append(chunk.strip())
            chunk = s + ". "
    chunks.append(chunk.strip())
    return chunks

# --- Embedding & Indexing ---
def build_vector_store(chunks):
    embeddings = model.encode(chunks)
    dim = embeddings[0].shape[0]
    index = faiss.IndexFlatL2(dim)
    index.add(np.array(embeddings))
    return index, chunks

# --- Grok (Mocked) ---
def query_grok(prompt):
    result = client.chat.completions.create(
    messages={
        {
        "role": "system",
        "content": "You are a Python programmer tasked with generating high quality Python code."
        "Your task is to Generate the best content possible for the user's request. If the user provides critique," 
        "respond with a revised version of your previous attempt."
    },
    {"role": "user",
    "content": prompt,}
    },
    model="llama3-70b-8192"
    ).choices[0].message.content

    return result
# --- Retrieval ---
def retrieve(query, index, chunks):
    query_embedding = model.encode([query])
    D, I = index.search(np.array(query_embedding), k=3)
    return [chunks[i] for i in I[0]]

# --- Answer Generation ---
def generate_answer(query):
    global vector_index, text_chunks
    context = "\n".join(retrieve(query, vector_index, text_chunks))
    prompt = f"Context:\n{context}\n\nQuestion: {query}\nAnswer:"
    return query_grok(prompt)

# --- Evaluation ---
def normalize(text):
    return re.sub(r'[^a-z0-9]', '', text.lower())

def evaluate_rag():
    dataset = load_dataset("trivia_qa", "unfiltered.nocontext", split="validation[:10]")
    correct = 0
    for item in dataset:
        question = item['question']
        gt_answers = [normalize(ans) for ans in item['answer']['aliases'] if ans]
        pred = normalize(generate_answer(question))
        if any(ans in pred for ans in gt_answers):
            correct += 1
    return {"accuracy": correct / len(dataset), "total": len(dataset), "correct": correct}

# --- Ingestion Pipeline ---
def ingest(seed_queries, site):
    global vector_index, text_chunks
    all_chunks = []
    for query in seed_queries:
        results = search_tavily(query, site=site)
        for r in results:
            all_chunks.extend(chunk_text(r))
    vector_index, text_chunks = build_vector_store(all_chunks)
    return {"message": f"Ingested {len(all_chunks)} chunks from {site}"}
