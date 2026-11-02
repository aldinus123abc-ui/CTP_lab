import database
import operation

def main():
    database.initilize_db()

    print("-----Insertion of students in the database------")
    number = int(input("Enter number of student data to be inserted: "))
    while(number):
        operation.add_student()
        number = number - 1

    operation.display_Students()

main()