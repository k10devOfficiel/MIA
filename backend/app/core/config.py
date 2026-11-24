from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Configuration globale de MIA, chargee depuis .env et validee par Pydantic."""

    llm_provider: Literal["ollama", "cloud"] = "ollama"
    ollama_url: str = "http://localhost:11434"
    ollama_model: str = "qwen2.5:3b"
    cloud_api_key: str = ""
    cloud_model: str = ""
    allowed_origins: str = "http://localhost:8000,http://127.0.0.1:8000"
    enable_local_tools: bool = False
    sandbox_dir: str = "sandbox"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    @property
    def allowed_origins_list(self) -> list[str]:
        """Convertit ALLOWED_ORIGINS en liste propre d'origines autorisees."""
        return [origin.strip() for origin in self.allowed_origins.split(",") if origin.strip()]


settings = Settings()
