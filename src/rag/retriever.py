from __future__ import annotations
from src.pln.embeddings import TextEmbedder
from src.rag.faiss_index import FaissStore

class SemanticRetriever:
    def __init__(self):
        self.embedder = TextEmbedder()
        self.store = None

    def fit(self, documents: list[dict]) -> None:
        texts = [f"{d.get('title', '')}. {d.get('text', '')}" for d in documents]
        emb = self.embedder.encode(texts)
        self.store = FaissStore(dim=emb.shape[1])
        self.store.add(emb, documents)

    def search(self, query: str, top_k: int = 5):
        q_emb = self.embedder.encode([query])
        return self.store.search(q_emb, top_k=top_k)
