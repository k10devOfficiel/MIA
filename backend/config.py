from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Configuration globale de MIA, chargee depuis le fichier .env."""

    app_env: str = "development"
    cors_origins: str = "http://localhost:8000"
    llm_provider: str = "ollama"
    ollama_base_url: str = "http://localhost:11434"
    ollama_model: str = "qwen2.5:3b"
    cloud_api_key: str = ""
    cloud_model: str = ""
    database_path: str = "data/mia.db"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    @property
    def cors_origins_list(self) -> list[str]:
        """Convertit la chaine CORS_ORIGINS en liste d'origines propres."""
        return [origin.strip() for origin in self.cors_origins.split(",") if origin.strip()]


settings = Settings()
