import sqlite3

def setup_employee_db():
    conn = sqlite3.connect('employees.db')
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS employees (
    emp_ID TEXT PRIMARY KEY,
    name TEXT,
    designation TEXT,
    salary REAL
    )
    """)
    conn.commit()
    return conn

def create_employee(conn, emp_id, name, dsgn,salary):
    c = conn.cursor()
    try:
        c.execute('INSERT INTO employees VALUES (?, ?, ?, ?)',(emp_id,name,dsgn,salary))
        conn.commit()
        print(f"Employee with emp_id {emp_id} and name {name} is inserted")
    except sqlite3.IntegrityError:
        print("This Employee already exist")

def read_employee(conn):
    c  = conn.execute('SELECT * FROM employees')
    print("\n------Employee Data------")
    for row in c:
        print(row)

def update_salary(conn,emp_id, new_salary):
    conn.execute('UPDATE employees SET salary = ? WHERE emp_id = ?', (emp_id, new_salary))
    conn.commit()
    print(f"Update salary for Emp ID: {emp_id}")

def delete_employees(conn, emp_id):
    conn.execute('DELETE FROM employees WHERE emp_id = ?', (emp_id))
    conn.commit()
    print(f"The employee with emp_id {emp_id} is deleted successfully")

conn = setup_employee_db()
create_employee(conn, 'E01','John','manager',68000)
read_employee(conn)
conn.close()
