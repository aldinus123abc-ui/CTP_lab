import database
import operation

def main():
    database.initilize_db()

    print("-----Insertion of Employees in the database------")

    number = int(input("Enter number of employee's data to be inserted: "))

    while(number):
        operation.create_employee()
        number = number - 1

    print("\n____Deletion of an employee_____")
    emp_id = input("Enter the employee id to be deleted :")
    operation.delete_employee(emp_id)

    print("\n______Updation of Employees Salary___________")
    emp_id = input("Enter the employee id to be updated: ")
    new_salary = float(input("Enter the new salary : "))
    operation.update_salary(emp_id, new_salary)

    operation.read_employee()

main()