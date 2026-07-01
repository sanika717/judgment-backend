from pathlib import Path

from pydantic_settings import BaseSettings
from pydantic import ConfigDict


BASE_DIR = Path(__file__).resolve().parent.parent


class Settings(BaseSettings):

    # --------------------------------------------------
    # Application
    # --------------------------------------------------

    APP_NAME: str = "AI Legal Judgement Assistant"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = True

    # --------------------------------------------------
    # Database
    # --------------------------------------------------

    DATABASE_URL: str

    # --------------------------------------------------
    # JWT
    # --------------------------------------------------

    SECRET_KEY: str
    ALGORITHM: str = "HS256"

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7

    # --------------------------------------------------
    # LLM
    # --------------------------------------------------

    LLM_PROVIDER: str = "ollama"

    OLLAMA_MODEL: str = "qwen2.5:3b"

    EMBEDDING_MODEL: str = "nomic-embed-text"

    # --------------------------------------------------
    # Vector Database
    # --------------------------------------------------

    CHROMA_PATH: str = "storage/chroma_db"

    # --------------------------------------------------
    # Storage
    # --------------------------------------------------

    UPLOAD_DIR: str = "storage/uploads"

    PROCESSED_DIR: str = "storage/processed"

    SUMMARY_DIR: str = "storage/summaries"

    AUDIO_DIR: str = "storage/audio"

    # --------------------------------------------------
    # OCR
    # --------------------------------------------------

    OCR_LANGUAGE: str = "en"

    # --------------------------------------------------
    # Translation
    # --------------------------------------------------

    DEFAULT_LANGUAGE: str = "English"

    # --------------------------------------------------
    # Logging
    # --------------------------------------------------

    LOG_LEVEL: str = "INFO"

    LOG_FILE: str = "logs/app.log"

    model_config = ConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()