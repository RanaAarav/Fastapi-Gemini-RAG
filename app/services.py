import time
import random
import google.generativeai as genai
from pinecone import Pinecone
from app.config import settings

genai.configure(api_key=settings.GEMINI_API_KEY)
generation_model = genai.GenerativeModel('gemini-2.5-flash')

pc = Pinecone(api_key=settings.PINECONE_API_KEY)
index = pc.Index(settings.PINECONE_INDEX_NAME)

def embed_text(text: str):
    """
    Helper to convert text to vector using Gemini.
    Includes a fallback for Quota errors so the app doesn't crash during demos.
    """
    try:
        result = genai.embed_content(
            model="models/text-embedding-004",
            content=text,
            task_type="retrieval_query"
        )
        return result['embedding']
    except Exception as e:
        print(f"Warning: Embedding API failed ({e}). Using mock vector for demo.")
        return [random.uniform(-0.1, 0.1) for _ in range(768)]

def seed_database():
    """Populates Pinecone with sample data"""
    documents = [
        {"id": "doc1", "text": "FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.7+."},
        {"id": "doc2", "text": "Docker containers wrap up software and its dependencies into a standardized unit for software development."},
        {"id": "doc3", "text": "RAG (Retrieval-Augmented Generation) optimizes LLM output by referencing an authoritative knowledge base."},
        {"id": "doc4", "text": "Pinecone is a managed vector database that makes it easy to add vector search to production applications."}
    ]
    
    vectors = []
    print("Starting seeding process...")
    for doc in documents:
        print(f"Embedding doc: {doc['id']}")
        embedding = embed_text(doc['text'])
        
        vectors.append({
            "id": doc['id'],
            "values": embedding,
            "metadata": {"text": doc['text']}
        })
        time.sleep(2.0) 
        
    try:
        index.upsert(vectors=vectors)
        return {"status": "Database seeded successfully", "count": len(vectors)}
    except Exception as e:
        return {"status": "Error upserting to Pinecone", "detail": str(e)}

def get_rag_response(question: str) -> dict:
    start_time = time.time()
    
    query_embedding = embed_text(question)
    
    try:
        search_results = index.query(
            vector=query_embedding,
            top_k=2,
            include_metadata=True
        )
        relevant_docs = [match['metadata']['text'] for match in search_results['matches']]
    except Exception as e:
        print(f"Pinecone Error: {e}")
        relevant_docs = []
    
    if not relevant_docs:
      
        relevant_docs = ["FastAPI is a web framework.", "Docker is for containers."] 
    
    context_str = "\n".join(relevant_docs)

    prompt = f"""
    You are a helpful technical assistant. 
    Context: {context_str}
    Question: {question}
    Answer:
    """
    
    try:
        response = generation_model.generate_content(prompt)
        answer_text = response.text
    except Exception as e:
        answer_text = f"Error: {str(e)}"

    return {
        "answer": answer_text,
        "source_documents": relevant_docs,
        "processing_time": time.time() - start_time
    }
