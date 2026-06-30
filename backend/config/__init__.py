from .settings import settings

BASE_DIR = settings.BASE_DIR
USER_DATA_DIR = settings.USER_DATA_DIR
DB_PATH = settings.DB_PATH
CHAT_HISTORY_DB_PATH = settings.CHAT_HISTORY_DB_PATH
OCR_MODE = settings.OCR_MODE
GEMINI_API_KEY = settings.GEMINI_API_KEY
GEMINI_MODEL = settings.GEMINI_MODEL
OLLAMA_MODEL = settings.OLLAMA_MODEL
OLLAMA_EMBED_MODEL = settings.OLLAMA_EMBED_MODEL

__all__ = [
    "settings",
    "BASE_DIR",
    "USER_DATA_DIR",
    "DB_PATH",
    "CHAT_HISTORY_DB_PATH",
    "OCR_MODE",
    "GEMINI_API_KEY",
    "GEMINI_MODEL",
    "OLLAMA_MODEL",
    "OLLAMA_EMBED_MODEL",
]
