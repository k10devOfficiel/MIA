from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from backend.app.core.config import settings


class HealthResponse(BaseModel):
    """Schema Pydantic pour la reponse de la route /health."""

    status: str


app = FastAPI(title="MIA Backend", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins_list,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)


@app.get("/health", response_model=HealthResponse)
def health_check() -> HealthResponse:
    """Verifie que le serveur FastAPI est en ligne."""
    return HealthResponse(status="ok")
