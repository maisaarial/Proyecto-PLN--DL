from pathlib import Path
from pydantic import BaseModel
import os

class Settings(BaseModel):
    app_name: str = os.getenv("APP_NAME", "chatbot-movilidad-bilbao")
    data_dir: Path = Path(os.getenv("DATA_DIR", "data"))
    embedding_model: str = os.getenv(
        "EMBEDDING_MODEL",
        "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
    )
    intent_model: str = os.getenv(
        "INTENT_MODEL",
        "dccuchile/bert-base-spanish-wwm-cased"
    )
    device: str = os.getenv("DEVICE", "cpu")

settings = Settings()
