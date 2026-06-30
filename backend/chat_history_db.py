# backend/chat_history_db.py
import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CHAT_HISTORY_DB_PATH = os.path.join(BASE_DIR, "chat_history.db")

# DB_PATH = os.path.join(BASE_DIR, "file_tracking.db")
from config import DB_PATH
# Create the history table if it doesn't exist
def init_chat_history_db():
    conn = sqlite3.connect(CHAT_HISTORY_DB_PATH)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT NOT NULL,
            session_id TEXT NOT NULL,
            user_message TEXT,
            ai_message TEXT
        )
    """)
    conn.commit()
    conn.close()

# Save user and AI message to history
def save_user_chat_history(user_id, session_id, user_message, ai_message):
    conn = sqlite3.connect(CHAT_HISTORY_DB_PATH)
    c = conn.cursor()
    c.execute("""
        INSERT INTO history (user_id, session_id, user_message, ai_message)
        VALUES (?, ?, ?, ?)
    """, (user_id, session_id, user_message, ai_message))
    conn.commit()
    conn.close()

# Fetch chat history for given user and session
def get_user_chat_history(user_id, session_id):
    conn = sqlite3.connect(CHAT_HISTORY_DB_PATH)
    c = conn.cursor()
    c.execute("""
        SELECT user_message, ai_message FROM history
        WHERE session_id = ?
        ORDER BY id ASC
    """, (session_id,))
    rows = c.fetchall()
    conn.close()

    # Return in message format for chat replay
    history = []
    for user_msg, ai_msg in rows:
        if user_msg:
            history.append({"role": "user", "message": user_msg})
        if ai_msg:
            history.append({"role": "ai", "message": ai_msg})
    return history



def get_all_sessions(user_id):
    conn = sqlite3.connect(CHAT_HISTORY_DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT DISTINCT session_id FROM history
        WHERE user_id = ?
        ORDER BY session_id ASC
    """, (user_id,))
    sessions = [row[0] for row in cursor.fetchall()]
    conn.close()
    return sessions





