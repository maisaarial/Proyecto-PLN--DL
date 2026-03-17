from __future__ import annotations
from typing import Dict

INTENT_KEYWORDS = {
    "consulta_trafico": ["tráfico", "trafico", "atasco", "retención", "retencion", "congestión"],
    "consulta_obras": ["obra", "obras", "corte", "ocupación", "ocupacion"],
    "consulta_ruta": ["ruta", "alternativa", "desvío", "desvio", "camino"],
    "consulta_general": [],
}

def predict_intent(text: str) -> Dict[str, float | str]:
    text_l = text.lower()
    scores = {k: 0 for k in INTENT_KEYWORDS}
    for intent, kws in INTENT_KEYWORDS.items():
        scores[intent] = sum(1 for kw in kws if kw in text_l)
    best = max(scores, key=scores.get)
    if scores[best] == 0:
        best = "consulta_general"
    return {"intent": best, "confidence": float(scores.get(best, 0))}
