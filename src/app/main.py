from __future__ import annotations
from fastapi import FastAPI
from pydantic import BaseModel
from src.app.pipeline import MobilityChatbotPipeline

app = FastAPI(title="Chatbot Movilidad Bilbao")
pipeline = MobilityChatbotPipeline()
pipeline.collect_documents()
if pipeline.documents:
    pipeline.build_index()

class QueryRequest(BaseModel):
    question: str

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/ask")
def ask(req: QueryRequest):
    return pipeline.ask(req.question)
