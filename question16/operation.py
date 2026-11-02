import sqlite3
from database import connect_db


def add_student():
    conn = connect_db()
    c = conn.cursor()
    roll = input("Enter scholar: ")
    name = input("Enter name: ")
    dept = input("Enter department: ")
    cgpa = float(input("Enter cgpa: "))
    print()
    try:
        c.execute('INSERT INTO students VALUES (?, ?, ?, ?)',(roll,name,dept,cgpa))
        conn.commit()
    except sqlite3.IntegrityError:
        print("Students with the same value already exists")
    conn.close()

def display_Students():
    conn = connect_db()
    c = conn.cursor()
    c.execute('SELECT * FROM students')
    records = c.fetchall()
    if not records:
        print("NO student record found")
    else:
        print("\n---------Students Records---------")
        for row in records:
            print(f"ScholarID: {row[0]}, Name: {row[1]}, Department: {row[2]}, CGPA: {row[3]}") 
    conn.close()