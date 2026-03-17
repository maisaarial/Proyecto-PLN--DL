from src.app.pipeline import MobilityChatbotPipeline

def main():
    pipeline = MobilityChatbotPipeline()
    docs = pipeline.collect_documents()
    print(f"Documentos recolectados: {len(docs)}")
    if docs:
        pipeline.build_index()
        response = pipeline.ask("¿Hay cortes de tráfico en Bilbao centro y alternativas de ruta?")
        print("\n===== RESPUESTA =====")
        print(response["answer"])
        print("\n===== NLP =====")
        print(response["nlp"])
        print("\n===== TOP DOCS =====")
        for d in response["retrieved_documents"][:3]:
            print(d["source"], "->", d["title"])

if __name__ == "__main__":
    main()
