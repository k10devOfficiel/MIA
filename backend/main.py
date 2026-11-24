from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from backend.config import settings


class HealthResponse(BaseModel):
    """Reponse typee pour la route de verification de sante."""

    status: str
    app: str


app = FastAPI(title="MIA Backend", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins_list,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)


@app.get("/health", response_model=HealthResponse)
def health_check() -> HealthResponse:
    """Verifie que le serveur FastAPI repond correctement."""
    return HealthResponse(status="ok", app="MIA")
