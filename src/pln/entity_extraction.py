from __future__ import annotations
import re
from typing import Dict

ZONE_PATTERNS = [
    "bilbao", "deusto", "abando", "recalde", "gran vía", "gran via",
    "moyúa", "moyua", "zabalburu", "basurto", "zurbaranbarri"
]
EVENT_PATTERNS = [
    "atasco", "obras", "accidente", "corte", "ocupación", "ocupacion",
    "aparcamiento", "retención", "retencion", "congestión", "congestion"
]

def extract_entities(text: str) -> Dict[str, list]:
    text_l = text.lower()
    zones = [z for z in ZONE_PATTERNS if z in text_l]
    events = [e for e in EVENT_PATTERNS if e in text_l]
    dates = re.findall(r"\b\d{1,2}[/-]\d{1,2}[/-]\d{2,4}\b", text)
    hours = re.findall(r"\b\d{1,2}:\d{2}\b", text)
    return {
        "zones": sorted(set(zones)),
        "event_types": sorted(set(events)),
        "dates": dates,
        "hours": hours,
    }
