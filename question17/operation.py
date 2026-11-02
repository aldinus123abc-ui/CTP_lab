import sqlite3
from database import connect_db

def create_employee():
    conn = connect_db()
    c = conn.cursor()
    emp_id = input("Enter employee id: ")
    name = input("Enter name: ")
    dsgn = input("Enter designation/post: ")
    salary = float(input("Enter salary: "))
    try:
        c.execute('INSERT INTO employees VALUES (?, ?, ?, ?)',(emp_id,name,dsgn,salary))
        conn.commit()
        print(f"Employee with emp_id {emp_id} and name {name} is inserted")
    except sqlite3.IntegrityError:
        print("This Employee already exist")
    conn.close()

def read_employee():
    conn = connect_db()
    c  = conn.execute('SELECT * FROM employees')
    print("\n------Employee Data------")
    for row in c:
        print(row)

def update_salary(emp_id, new_salary):
    conn = connect_db()
    conn.execute('UPDATE employees SET salary = ? WHERE emp_id = ?', (emp_id, new_salary))
    conn.commit()
    print(f"Update salary for Emp ID: {emp_id}")

def delete_employee(emp_id):
    conn = connect_db()
    conn.execute('DELETE FROM employees WHERE emp_id = ?', (emp_id,))
    conn.commit()
    print(f"The employee with emp_id {emp_id} is deleted successfully")
    
