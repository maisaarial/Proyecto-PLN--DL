from __future__ import annotations
from dataclasses import dataclass, asdict
from typing import Optional, List

@dataclass
class TrafficRecord:
    source: str
    title: str
    text: str
    published_at: Optional[str] = None
    url: Optional[str] = None
    zone: Optional[str] = None
    event_type: Optional[str] = None

    def to_dict(self):
        return asdict(self)

@dataclass
class UserQuery:
    text: str

@dataclass
class NLPResult:
    intent: str
    entities: dict

@dataclass
class VisualResult:
    label: str
    score: float

@dataclass
class RetrievalResult:
    documents: List[dict]

@dataclass
class ChatbotResponse:
    answer: str
    nlp: dict
    retrieved_documents: List[dict]
    visual_signal: Optional[dict] = None
