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


