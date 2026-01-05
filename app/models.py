from pydantic import BaseModel, Field
from typing import List

class QueryRequest(BaseModel):
    question: str = Field(..., min_length=3, description="The user's question")
    
class QueryResponse(BaseModel):
    answer: str
    source_documents: List[str]
    processing_time: float