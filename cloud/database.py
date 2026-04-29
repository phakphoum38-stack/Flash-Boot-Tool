import sqlite3

conn = sqlite3.connect("cloud.db", check_same_thread=False)
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS fixes (
    id INTEGER PRIMARY KEY,
    signature TEXT,
    strategies TEXT,
    success INTEGER,
    uses INTEGER DEFAULT 0
)
""")

conn.commit()
