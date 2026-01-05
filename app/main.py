from fastapi import FastAPI, HTTPException
from app.models import QueryRequest, QueryResponse
from app.services import get_rag_response, seed_database 

app = FastAPI(title="Production Gemini RAG API", version="1.0.0")

@app.get("/health")
def health_check():
    """Liveness probe for Kubernetes"""
    return {"status": "healthy", "service": "rag-api"}

@app.post("/query", response_model=QueryResponse)
def query_endpoint(request: QueryRequest):
    try:
        result = get_rag_response(request.question)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.post("/seed")
def seed_endpoint():
    """One-time endpoint to populate Pinecone with data"""
    try:
        return seed_database()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))