import pytest
from fastapi.testclient import TestClient
from pydantic import ValidationError

from backend.app.core.config import Settings
from backend.app.main import app

client = TestClient(app)


def test_health_returns_ok() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_settings_rejects_invalid_llm_provider() -> None:
    with pytest.raises(ValidationError):
        Settings(llm_provider="fournisseur_inconnu")
