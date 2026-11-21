import sqlite3

DB_NAME = "company_payroll.db"


def initialize_database(conn):
    """Creates tables and inserts sample employee records if the database is empty."""
    cursor = conn.cursor()

    cursor.execute("PRAGMA foreign_keys = ON;")

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS departments (
            dept_id INTEGER PRIMARY KEY AUTOINCREMENT,
            dept_name TEXT UNIQUE NOT NULL
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            emp_id INTEGER PRIMARY KEY AUTOINCREMENT,
            emp_name TEXT NOT NULL,
            designation TEXT NOT NULL,
            salary REAL NOT NULL,
            dept_id INTEGER NOT NULL,
            FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
        );
    """)

    cursor.execute("SELECT COUNT(*) FROM departments;")
    if cursor.fetchone()[0] == 0:
        departments = [("Engineering",), ("Human Resources",), ("Finance",), ("Marketing",)]
        cursor.executemany("INSERT INTO departments (dept_name) VALUES (?);", departments)

        employees = [
            ("Aarav Sharma", "Senior Developer", 125000.00, 1),
            ("Diya Patel", "Backend Engineer", 98000.00, 1),
            ("Rohan Verma", "DevOps Specialist", 110000.00, 1),
            ("Ananya Nair", "HR Manager", 85000.00, 2),
            ("Kabir Das", "Talent Acquisition", 62000.00, 2),
            ("Meera Iyer", "Financial Analyst", 92000.00, 3),
            ("Vikram Singh", "Senior Accountant", 78000.00, 3),
            ("Sneha Roy", "Marketing Lead", 88000.00, 4),
        ]
        cursor.executemany("""
            INSERT INTO employees (emp_name, designation, salary, dept_id)
            VALUES (?, ?, ?, ?);
        """, employees)

    conn.commit()


def generate_summary_report(conn, min_salary=0.0):
    """Generates a department-wise salary summary filtered by minimum salary."""
    cursor = conn.cursor()

    query = """
        SELECT 
            d.dept_name,
            COUNT(e.emp_id) AS headcount,
            COALESCE(MIN(e.salary), 0) AS min_sal,
            COALESCE(MAX(e.salary), 0) AS max_sal,
            COALESCE(AVG(e.salary), 0) AS avg_sal,
            COALESCE(SUM(e.salary), 0) AS total_sal
        FROM departments d
        LEFT JOIN employees e 
            ON d.dept_id = e.dept_id AND e.salary >= ?
        GROUP BY d.dept_id, d.dept_name
        ORDER BY total_sal DESC;
    """

    cursor.execute(query, (min_salary,))
    rows = cursor.fetchall()

    print(f"\n=== Department-Wise Salary Summary (Min Salary Filter: ₹{min_salary:,.2f}) ===")
    print("-" * 86)
    print(f"{'Department':<18} {'Staff':<7} {'Min (₹)':<14} {'Max (₹)':<14} {'Avg (₹)':<14} {'Total (₹)':<15}")
    print("-" * 86)

    grand_total = 0.0
    for dept_name, count, min_s, max_s, avg_s, total_s in rows:
        grand_total += total_s
        print(f"{dept_name:<18} {count:<7} {min_s:<14,.2f} {max_s:<14,.2f} {avg_s:<14,.2f} {total_s:<15,.2f}")

    print("-" * 86)
    print(f"{'TOTAL PAYROLL':<71} ₹{grand_total:,.2f}\n")


def generate_department_detail(conn, department_name):
    """Fetches detailed employee salary records for a specific department."""
    cursor = conn.cursor()

    query = """
        SELECT e.emp_id, e.emp_name, e.designation, e.salary
        FROM employees e
        INNER JOIN departments d ON e.dept_id = d.dept_id
        WHERE LOWER(d.dept_name) = LOWER(?)
        ORDER BY e.salary DESC;
    """

    cursor.execute(query, (department_name.strip(),))
    employees = cursor.fetchall()

    if not employees:
        print(f"\nNo records found for department: '{department_name}'.\n")
        return

    print(f"\n=== Detailed Salary Report: {department_name.title()} ===")
    print("-" * 64)
    print(f"{'ID':<6} {'Employee Name':<20} {'Designation':<22} {'Salary (₹)':<12}")
    print("-" * 64)

    dept_total = 0.0
    for emp_id, name, role, salary in employees:
        dept_total += salary
        print(f"{emp_id:<6} {name:<20} {role:<22} {salary:<12,.2f}")

    print("-" * 64)
    print(f"{'Department Subtotal':<48} ₹{dept_total:,.2f}\n")


def main():
    with sqlite3.connect(DB_NAME) as conn:
        initialize_database(conn)

        while True:
            print("=== Employee Salary Reporting System ===")
            print("1. Department-Wise Salary Summary (All Employees)")
            print("2. Department-Wise Summary (Filter by Minimum Salary)")
            print("3. Detailed Report for a Specific Department")
            print("4. Exit")

            choice = input("Select an option (1-4): ").strip()

            if choice == "1":
                generate_summary_report(conn)
            elif choice == "2":
                try:
                    threshold = float(input("Enter minimum salary threshold (₹): "))
                    generate_summary_report(conn, min_salary=threshold)
                except ValueError:
                    print("Invalid amount. Please enter a numeric value.\n")
            elif choice == "3":
                dept = input("Enter Department Name (e.g., Engineering, Finance): ")
                generate_department_detail(conn, dept)
            elif choice == "4":
                print("Closing database connection. Goodbye!")
                break
            else:
                print("Invalid option. Please choose between 1 and 4.\n")


if __name__ == "__main__":
    main()
