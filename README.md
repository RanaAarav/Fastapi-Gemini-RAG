# Production-Ready RAG API with FastAPI, Gemini, and Pinecone

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.109-009688)
![Docker](https://img.shields.io/badge/Docker-Enabled-2496ED)
![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen)

A robust, containerized REST API that implements **Retrieval-Augmented Generation (RAG)** using **Google Gemini** (LLM & Embeddings) and **Pinecone** (Vector Database).

This project demonstrates how to move beyond Jupyter Notebooks and build a scalable AI backend with input validation, error handling, and modular architecture.

*   **RAG Architecture:** Retrieves context from a vector database before answering.
*   **Vector Search:** Uses **Pinecone** for high-performance semantic search.
*   **Dockerized:** Multi-stage build for small, secure production images.

## Tech Stack

*   **Framework:** FastAPI
*   **Language:** Python 3.9
*   **AI Models:** Google Gemini 2.5 Flash (Generation), Text-Embedding-004 (Embeddings)
*   **Database:** Pinecone (Serverless Vector DB)
*   **Deployment:** Docker / Kubernetes Ready

---

## Quick Start (Local)

### 1. Prerequisites
*   Python 3.9
*   A [Pinecone](https://www.pinecone.io/) API Key (Create an Index with **768 dimensions**).
*   A [Google Gemini](https://ai.google.dev/) API Key.

### 2. Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/RanaAarav/Fastapi-Gemini-RAG.git
cd Fastapi-Gemini-RAG
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## 3. Configuration

Create a `.env` file in the root directory:

```ini
GEMINI_API_KEY=your_google_api_key
PINECONE_API_KEY=your_pinecone_api_key
```

## 4. Run the API

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```arduino
[uvicorn app.main:app --reload](http://localhost:8000)
```

## Running with Docker

Build and run the containerized application:

```bash
docker build -t gemini-rag .
docker run -p 8000:8000 --env-file .env gemini-rag
```

## Usage

### 1. Seed the Database

Since the Pinecone index starts empty, seed it with sample data:

```bash
curl -X POST http://localhost:8000/seed
```
Response:

```json
{
  "status": "Database seeded successfully",
  "count": 4
}
```

### 2. Query the AI

Ask a question. The system retrieves context from Pinecone and answers based on facts:

```bash
curl -X POST "http://localhost:8000/query" \
  -H "Content-Type: application/json" \
  -d '{"question": "What is RAG?"}'
```

Response:

```json
{
  "answer": "RAG (Retrieval-Augmented Generation) optimizes LLM output by referencing an authoritative knowledge base...",
  "source_documents": [
    "RAG (Retrieval-Augmented Generation) optimizes LLM output..."
  ],
  "processing_time": 1.24
}
```
### 3. API Documentation

Interactive Swagger UI:

```bash
http://localhost:8000/docs
```

## Project Structure

'''
├── app/
│   ├── __init__.py
│   ├── main.py          # API endpoints & entry point
│   ├── models.py        # Pydantic schemas
│   ├── services.py      # Business logic (Gemini + Pinecone)
│   └── config.py        # Environment configuration
├── Dockerfile           # Multi-stage production build
├── requirements.txt     # Python dependencies
└── .env                 # Secrets (not committed to Git)
'''

## License

MIT
