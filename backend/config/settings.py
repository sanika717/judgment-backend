import os
from pathlib import Path
from pydantic_settings import BaseSettings

BASE_DIR_PATH = Path(__file__).resolve().parent.parent
STORAGE_DIR = BASE_DIR / "storage"
UPLOADS_DIR = STORAGE_DIR / "uploads"
PROCESSED_DIR = STORAGE_DIR / "processed"
DB_DIR = BASE_DIR / "data"
USER_DATA_DIR = BASE_DIR / "user_data"

class Settings(BaseSettings):
    PROJECT_NAME: str = "AI Legal Judgement Assistant"
    PROJECT_VERSION: str = "0.1.0"
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = os.getenv("SECRET_KEY", "change_me_securely")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "60"))
    BACKEND_CORS_ORIGINS: list[str] = ["*"]
    SQLALCHEMY_DATABASE_URI: str = os.getenv(
        "SQLALCHEMY_DATABASE_URI",
        f"sqlite:///{DB_DIR / 'app.db'}"
    )
    USER_DATA_DIR: str = str(USER_DATA_DIR)
    STORAGE_UPLOAD_DIR: str = str(UPLOADS_DIR)
    STORAGE_PROCESSED_DIR: str = str(PROCESSED_DIR)
    BASE_DIR: str = str(BASE_DIR_PATH)
    DB_PATH: str = os.getenv("DB_PATH", str(BASE_DIR_PATH / "file_tracking.db"))
    CHAT_HISTORY_DB_PATH: str = os.getenv("CHAT_HISTORY_DB_PATH", str(BASE_DIR_PATH / "chat_history.db"))
    OCR_MODE: str = os.getenv("OCR_MODE", "gemini")
    GEMINI_API_KEY: str | None = os.getenv("GEMINI_API_KEY")
    GEMINI_MODEL: str = os.getenv("GEMINI_MODEL", "gemini-1.5-pro")
    LLM_PROVIDER: str = os.getenv("LLM_PROVIDER", "ollama")
    OLLAMA_MODEL: str = os.getenv("OLLAMA_MODEL", "mistral")
    OLLAMA_EMBED_MODEL: str = os.getenv("OLLAMA_EMBED_MODEL", "nomic-embed-text")

    class Config:
        env_file = BASE_DIR_PATH / ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"

settings = Settings()

for path in [STORAGE_DIR, UPLOADS_DIR, PROCESSED_DIR, DB_DIR, Path(settings.USER_DATA_DIR)]:
    os.makedirs(path, exist_ok=True)
