import sqlite3

def connect_db():
    return sqlite3.connect('students.db')

def initilize_db():
    conn = connect_db()
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS students (
    ScholarID TEXT PRIMARY KEY,
    Name TEXT,
    Department TEXT,
    CGPA REAL
    )
    """)
    conn.commit()
    conn.close()