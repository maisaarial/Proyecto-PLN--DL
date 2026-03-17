from __future__ import annotations
import faiss
import numpy as np

class FaissStore:
    def __init__(self, dim: int):
        self.index = faiss.IndexFlatIP(dim)
        self.documents = []

    def add(self, embeddings: np.ndarray, documents: list[dict]) -> None:
        self.index.add(embeddings.astype("float32"))
        self.documents.extend(documents)

    def search(self, query_embedding: np.ndarray, top_k: int = 5):
        scores, idxs = self.index.search(query_embedding.astype("float32"), top_k)
        results = []
        for score, idx in zip(scores[0], idxs[0]):
            if idx == -1:
                continue
            doc = dict(self.documents[idx])
            doc["score"] = float(score)
            results.append(doc)
        return results
