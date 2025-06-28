from fastapi import FastAPI, Query
from pydantic import BaseModel
from rag_utils import ingest, generate_answer, evaluate_rag

app = FastAPI(title="RAG with Tavily + Grok")

class IngestRequest(BaseModel):
    seed_queries: list
    site: str

class QuestionRequest(BaseModel):
    question: str

@app.post("/ingest")
def ingest_website(req: IngestRequest):
    return ingest(req.seed_queries, req.site)

@app.post("/answer")
def answer_question(req: QuestionRequest):
    return {"answer": generate_answer(req.question)}

@app.get("/evaluate")
def evaluate():
    return evaluate_rag()
