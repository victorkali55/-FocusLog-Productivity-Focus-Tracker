# database.py
import sqlite3
import os
from datetime import datetime

DB_NAME = "data/focuslog.db"

def create_tables():
    """Create database and tables if not exists."""
    if not os.path.exists("data"):
        os.makedirs("data")

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sessions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            project_name TEXT NOT NULL,
            start_time TEXT NOT NULL,
            end_time TEXT NOT NULL,
            duration INTEGER NOT NULL,  -- in minutes
            date TEXT NOT NULL
        )
    ''')

    conn.commit()
    conn.close()

def add_session(project_name, start_time, end_time):
    """Add a new work session to the database."""
    duration = int((end_time - start_time).total_seconds() // 60)
    date_str = start_time.strftime("%Y-%m-%d")

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO sessions (project_name, start_time, end_time, duration, date)
        VALUES (?, ?, ?, ?, ?)
    ''', (project_name, start_time.isoformat(), end_time.isoformat(), duration, date_str))
    conn.commit()
    conn.close()

def get_daily_total(date_str):
    """Get total minutes worked on a specific date."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT SUM(duration) FROM sessions WHERE date = ?', (date_str,))
    result = cursor.fetchone()[0]
    conn.close()
    return result or 0

def get_all_sessions():
    """Get all sessions (for debugging or export)."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM sessions ORDER BY start_time DESC')
    rows = cursor.fetchall()
    conn.close()
    return rows