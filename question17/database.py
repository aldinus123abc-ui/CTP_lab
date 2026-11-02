import sqlite3

def connect_db():
    return sqlite3.connect('students.db')

def initilize_db():
    conn = connect_db()
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS employees (
    emp_id TEXT PRIMARY KEY,
    name TEXT,
    designation TEXT,
    salary REAL
    )
    """)
    conn.commit()
    conn.close()