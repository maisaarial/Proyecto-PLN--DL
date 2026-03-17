from __future__ import annotations

def build_answer(user_query: str, retrieved_docs: list[dict], visual_signal: dict | None = None) -> str:
    if not retrieved_docs:
        base = "No encontré incidencias claras en las fuentes consultadas."
    else:
        top = retrieved_docs[:3]
        snippets = []
        for d in top:
            title = d.get("title", "")
            text = d.get("text", "")
            snippets.append(f"- {title}: {text[:180]}")
        base = "He encontrado esta información relevante:\n" + "\n".join(snippets)

    if visual_signal:
        base += (
            f"\n\nAnálisis visual de cámara: nivel estimado '{visual_signal['label']}' "
            f"con score {visual_signal['score']:.3f}."
        )

    if "ruta" in user_query.lower() or "alternativa" in user_query.lower():
        base += "\n\nCon base en las incidencias detectadas, conviene evitar los puntos afectados y consultar rutas alternativas."
    return base
