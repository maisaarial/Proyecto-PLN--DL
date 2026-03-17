from __future__ import annotations
from src.data_sources.bilbao_avisos import BilbaoAvisosSource
from src.data_sources.trafikoa_euskadi import TrafikoaEuskadiSource
from src.data_sources.deia_trafico import DeiaTraficoSource
from src.data_sources.x_source import XOfficialSource
from src.pln.text_cleaning import clean_text
from src.pln.intent_classifier import predict_intent
from src.pln.entity_extraction import extract_entities
from src.rag.retriever import SemanticRetriever
from src.rag.generator import build_answer

class MobilityChatbotPipeline:
    def __init__(self):
        self.sources = [
            BilbaoAvisosSource(),
            TrafikoaEuskadiSource(),
            DeiaTraficoSource(),
            XOfficialSource(),
        ]
        self.retriever = SemanticRetriever()
        self.documents = []

    def collect_documents(self):
        docs = []
        for source in self.sources:
            try:
                records = source.fetch()
                for r in records:
                    data = r.to_dict()
                    data["text"] = clean_text(data.get("text", ""))
                    data["title"] = clean_text(data.get("title", ""))
                    docs.append(data)
            except Exception as e:
                print(f"[WARN] Falló la fuente {source.source_name}: {e}")
        self.documents = docs
        return docs

    def build_index(self):
        if not self.documents:
            self.collect_documents()
        if self.documents:
            self.retriever.fit(self.documents)

    def ask(self, query: str, visual_signal: dict | None = None):
        intent = predict_intent(query)
        entities = extract_entities(query)
        retrieved = self.retriever.search(query, top_k=5) if self.documents else []
        answer = build_answer(query, retrieved, visual_signal=visual_signal)
        return {
            "answer": answer,
            "nlp": {
                "intent": intent,
                "entities": entities,
            },
            "retrieved_documents": retrieved,
            "visual_signal": visual_signal,
        }
