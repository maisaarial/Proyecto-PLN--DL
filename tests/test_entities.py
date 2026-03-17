from src.pln.entity_extraction import extract_entities

def test_extract_entities():
    text = "Hay corte de tráfico en Gran Vía hoy a las 10:30 por obras."
    ents = extract_entities(text)
    assert "gran vía" in ents["zones"] or "gran via" in ents["zones"]
    assert "corte" in ents["event_types"] or "obras" in ents["event_types"]
