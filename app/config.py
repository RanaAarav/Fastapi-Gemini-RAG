from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    GEMINI_API_KEY: str
    PINECONE_API_KEY: str
    PINECONE_INDEX_NAME: str = "rag-demo"
    
    class Config:
        env_file = ".env"

settings = Settings()
