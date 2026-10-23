import sqlite3

def get_sqlite_connection():
    """Bases en Memoria - H2, SQLite"""
    return sqlite3.connect(":memory:", check_same_thread=False)
