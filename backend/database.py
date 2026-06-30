# database.py
import sqlite3
import os
from config import DB_PATH, USER_DATA_DIR

import sqlite3
from config import DB_PATH  # Make sure this points to your SQLite file

def init_db():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    # 1. Ensure the 'uploads' table exists first
    c.execute('''
        CREATE TABLE IF NOT EXISTS uploads (
            user_id TEXT,
            filename TEXT
        )
    ''')
    conn.commit()

    # 2. Now check for 'session_id' column and add it if missing
    c.execute("PRAGMA table_info(uploads)")
    columns = [row[1] for row in c.fetchall()]
    if "session_id" not in columns:
        try:
            c.execute("ALTER TABLE uploads ADD COLUMN session_id TEXT")
            conn.commit()
        except sqlite3.OperationalError as e:
            print(f"Warning: ALTER TABLE failed: {e}")

    conn.close()

# ---------- FILE TRACKING ----------
def insert_file_record(user_id, filename, session_id=None):
    filename = filename.strip().lower()
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            "INSERT INTO uploads (user_id, filename, session_id) VALUES (?, ?, ?)",
            (user_id, filename, session_id)
        )
        conn.commit()

def file_record_exists(user_id, filename, session_id=None):
    filename = filename.strip().lower()
    with sqlite3.connect(DB_PATH) as conn:
        cur = conn.execute(
            "SELECT 1 FROM uploads WHERE user_id=? AND filename=? AND session_id=? LIMIT 1",
            (user_id, filename, session_id)
        )
        return cur.fetchone() is not None

def list_user_files(user_id, session_id=None):
    with sqlite3.connect(DB_PATH) as conn:
        if session_id:
            cur = conn.execute(
                "SELECT DISTINCT filename FROM uploads WHERE user_id=? AND session_id=?",
                (user_id, session_id)
            )
        else:
            cur = conn.execute(
                "SELECT DISTINCT filename FROM uploads WHERE user_id=?",
                (user_id,)
            )
        return [row[0] for row in cur.fetchall()]


def delete_user_file_record(user_id, filename, session_id=None):
    filename = filename.lower().strip()
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            "DELETE FROM uploads WHERE user_id=? AND filename=? AND session_id=?",
            (user_id, filename, session_id)
        )
        conn.commit()

# ---------- CHAT HISTORY PER USER (RAW MODE) ----------

def insert_new_session(user_id: str, session_id: str):
    user_dir = os.path.join(USER_DATA_DIR, user_id)
    os.makedirs(user_dir, exist_ok=True)
    db_path = os.path.join(user_dir, "chat_history.db")

    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS sessions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT,
            session_id TEXT
        )
    ''')
    c.execute("INSERT INTO sessions (user_id, session_id) VALUES (?, ?)", (user_id, session_id))
    conn.commit()
    conn.close()




def init_user_table():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE,
                password TEXT
            )
        """)
        conn.commit()

def create_user(username: str, password: str):
    """Insert a new user (username must be unique)"""
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (username, password)
        )
        conn.commit()

def get_user_by_username(username: str):
    """Retrieve user row by username"""
    with sqlite3.connect(DB_PATH) as conn:
        conn.row_factory = sqlite3.Row
        cur = conn.execute(
            "SELECT id, username, password FROM users WHERE username=?",
            (username,)
        )
        return cur.fetchone()
