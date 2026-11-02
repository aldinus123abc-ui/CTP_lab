import sqlite3

def setup_employee_db():
    conn = sqlite3.connect('students.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS students (
    ScholarID TEXT PRIMARY KEY,
    Name TEXT,
    Department TEXT,
    CGPA REAL
    )
    """)
    conn.commit()
    return conn

def add_student(conn, roll, name, dept, cgpa):
    c = conn.cursor()
    try:
        c.execute('INSERT INTO students VALUES (?, ?, ?, ?)',(roll,name,dept,cgpa))
        conn.commit()
    except sqlite3.IntegrityError:
        print("Students with the same value already exists")

def display_Students(conn):
    c = conn.cursor()
    c.execute('SELECT * FROM students')
    records = c.fetchall()
    print("\n---------Students Records---------")
    for row in records:
        print(f"ScholarID: {row[0]}, Name: {row[1]}, Department: {row[2]}, CGPA: {row[3]}")

conn = setup_employee_db()
add_student(conn,'CS126','Sushant','CSE',8.47)
display_Students(conn)
conn.close()