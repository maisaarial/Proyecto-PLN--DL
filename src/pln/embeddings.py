from __future__ import annotations
from sentence_transformers import SentenceTransformer
from config.settings import settings

class TextEmbedder:
    def __init__(self, model_name: str | None = None):
        self.model_name = model_name or settings.embedding_model
        self.model = SentenceTransformer(self.model_name)

    def encode(self, texts: list[str]):
        return self.model.encode(texts, convert_to_numpy=True, normalize_embeddings=True)
