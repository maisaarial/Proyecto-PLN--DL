# Proyecto conjunto PLN + Deep Learning
## Chatbot para consultas sobre movilidad urbana (Bilbao)

Este repositorio está organizado para que quede **claramente separado** qué corresponde a:

- **Minería de Texto y Procesamiento de Lenguaje Natural (PLN)**
- **Deep Learning e Inteligencia Artificial Generativa (DL/IAG)**

## Objetivo
Construir un chatbot que consulte incidencias de movilidad urbana en el área de Bilbao a partir de:
- portales oficiales de tráfico
- avisos municipales
- redes sociales oficiales
- medios digitales
- cámaras de tráfico

El sistema debe poder:
1. recuperar información textual reciente,
2. extraer entidades e intención del usuario,
3. buscar incidencias relevantes,
4. analizar imágenes de cámaras para estimar congestión,
5. generar una respuesta natural.

---

## Estructura del proyecto

```text
proyecto_chatbot_movilidad/
├── config/
├── data/
│   ├── raw/
│   ├── interim/
│   ├── processed/
│   └── examples/
├── notebooks/
│   ├── pln/
│   └── dl/
├── src/
│   ├── common/
│   ├── data_sources/
│   ├── pln/
│   ├── dl/
│   ├── rag/
│   └── app/
├── scripts/
├── tests/
├── requirements.txt
├── .env.example
└── README.md
```

---

## Separación por materias

### 1) MINERÍA DE TEXTO Y PLN
Incluye:
- scraping / parsing de texto desde fuentes web
- normalización y limpieza textual
- clasificación de intención
- extracción de entidades
- recuperación estructurada
- embeddings textuales
- evaluación NLP (accuracy, precision, recall, F1)

Carpetas principales:
- `src/data_sources/`
- `src/pln/`
- `notebooks/pln/`

### 2) DEEP LEARNING E IA GENERATIVA
Incluye:
- análisis de imágenes de cámaras
- clasificación de congestión
- detección automática de incidencias visuales
- búsqueda semántica con FAISS
- generador de respuestas tipo RAG
- evaluación DL (accuracy, F1, mAP si luego hacéis detección)

Carpetas principales:
- `src/dl/`
- `src/rag/`
- `notebooks/dl/`

---

## Flujo general del sistema

1. **Ingesta**
   - Se consultan fuentes web.
   - Se guardan textos e imágenes en `data/raw/`.

2. **Procesamiento PLN**
   - Se limpian los textos.
   - Se extraen entidades como: zona, tipo de incidencia, fecha, vía.
   - Se clasifica la intención del usuario.

3. **Procesamiento DL**
   - Se analizan imágenes de cámaras.
   - Se estima nivel de congestión o incidencia visual.

4. **Recuperación**
   - Los textos procesados se vectorizan.
   - Se indexan en FAISS para búsqueda semántica.

5. **Generación**
   - Un generador construye una respuesta final usando evidencias textuales + señal visual.

6. **API / chatbot**
   - FastAPI expone un endpoint para consultar el sistema.

---

## Ejecución rápida

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\activate  # Windows

pip install -r requirements.txt
cp .env.example .env

python scripts/run_pipeline_demo.py
uvicorn src.app.main:app --reload
```

---

## Qué está implementado en este scaffold
- estructura completa de proyecto
- scrapers base para fuentes HTML
- pipeline de PLN
- pipeline DL para clasificación de congestión por imagen
- índice semántico con FAISS
- API FastAPI
- configuración centralizada
- scripts de demo

## Qué tendréis que completar vosotros
- endpoint/API final real de algunas fuentes
- dataset real de cámaras
- dataset etiquetado para intención y entidades
- fine-tuning real de modelos
- validación experimental de la memoria

---

## Ideas de entregables por materia

### Entregable PLN
- dataset textual
- etiquetas de intención
- entidades anotadas
- evaluación de clasificación y extracción
- recuperación estructurada

### Entregable DL/IAG
- dataset de imágenes de tráfico
- modelo de clasificación de congestión
- embeddings + FAISS
- generador de respuesta tipo RAG
- comparación de modelos
