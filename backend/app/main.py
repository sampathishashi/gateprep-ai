from fastapi import FastAPI
from app.database import client


app = FastAPI(
    title="GATEPrep AI API",
    description="RAG-based GATE Study Assistant",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "GATEPrep AI Backend is running!"
    }


@app.get("/health")
def health_check():
    try:
        client.admin.command("ping")

        return {
            "status": "healthy",
            "database": "connected"
        }

    except Exception as e:
        return {
            "status": "unhealthy",
            "database": "disconnected",
            "error": str(e)
        }