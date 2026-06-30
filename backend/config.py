import os
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
USER_DATA_DIR = os.path.join(BASE_DIR, "user_data")
DB_PATH = os.path.join(BASE_DIR, "file_tracking.db")
CHAT_HISTORY_DB_PATH = os.path.join(BASE_DIR, "chat_history.db")

# Gemini config
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-1.5-pro")
OCR_MODE = os.getenv("OCR_MODE", "gemini")  # local or gemini

os.makedirs(USER_DATA_DIR, exist_ok=True)
