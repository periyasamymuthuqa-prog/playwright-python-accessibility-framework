import sqlite3
import pytest


@pytest.fixture(scope="session")
def db_connection():
    """Creates an in-memory SQLite database to demonstrate SQL test validation."""
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE users (
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            role TEXT NOT NULL,
            is_active INTEGER NOT NULL
        )
    """)
    cursor.executemany(
        "INSERT INTO users (username, role, is_active) VALUES (?, ?, ?)",
        [
            ("standard_user", "QA_Lead", 1),
            ("locked_out_user", "Tester", 0),
        ],
    )
    conn.commit()
    yield conn
    conn.close()
