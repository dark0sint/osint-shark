# Module to handle database operations using SQLite.

import sqlite3
from config import DATABASE_PATH

def init_db():
    """Initialize the SQLite database."""
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS osint_data 
                      (id INTEGER PRIMARY KEY, timestamp TEXT, data TEXT)''')
    conn.commit()
    conn.close()

def save_data(timestamp, data):
    """Save processed data to the database."""
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO osint_data (timestamp, data) VALUES (?, ?)", (timestamp, data))
    conn.commit()
    conn.close()
