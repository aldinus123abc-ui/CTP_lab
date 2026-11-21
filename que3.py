def add_student(records):
    """Inserts a new student dictionary into the records list."""
    roll_no = input("Enter Roll Number: ").strip()
    
    for student in records:
        if student["roll_no"] == roll_no:
            print(f"Error: Student with Roll No '{roll_no}' already exists.\n")
            return

    name = input("Enter Student Name: ").strip()
    course = input("Enter Course/Stream: ").strip()
    
    try:
        marks = float(input("Enter Percentage/Marks: "))
    except ValueError:
        print("Invalid input for marks. Setting marks to 0.0.")
        marks = 0.0

    student_record = {
        "roll_no": roll_no,
        "name": name,
        "course": course,
        "marks": marks
    }
    
    records.append(student_record)
    print(f"Success: Record for '{name}' added.\n")


def search_student(records):
    """Searches for a student by Roll Number or Name."""
    if not records:
        print("No records available to search.\n")
        return

    query = input("Enter Roll Number or Name to search: ").strip().lower()
    found_students = []

    for student in records:
        if query == student["roll_no"].lower() or query in student["name"].lower():
            found_students.append(student)

    if found_students:
        print(f"\nFound {len(found_students)} matching record(s):")
        print("-" * 55)
        print(f"{'Roll No':<12} {'Name':<20} {'Course':<12} {'Marks':<8}")
        print("-" * 55)
        for s in found_students:
            print(f"{s['roll_no']:<12} {s['name']:<20} {s['course']:<12} {s['marks']:<8.2f}")
        print("-" * 55 + "\n")
    else:
        print("No matching student record found.\n")


def delete_student(records):
    """Deletes a student record using their unique Roll Number."""
    if not records:
        print("No records available to delete.\n")
        return

    roll_no = input("Enter the Roll Number of the student to delete: ").strip()

    for index, student in enumerate(records):
        if student["roll_no"] == roll_no:
            removed = records.pop(index)
            print(f"Success: Record for '{removed['name']}' (Roll No: {roll_no}) deleted.\n")
            return

    print(f"Error: No student found with Roll No '{roll_no}'.\n")


def display_all(records):
    """Displays all student records in a formatted table."""
    if not records:
        print("Student database is currently empty.\n")
        return

    print("\nAll Student Records:")
    print("-" * 55)
    print(f"{'Roll No':<12} {'Name':<20} {'Course':<12} {'Marks':<8}")
    print("-" * 55)
    for s in records:
        print(f"{s['roll_no']:<12} {s['name']:<20} {s['course']:<12} {s['marks']:<8.2f}")
    print("-" * 55 + "\n")


def main():
    student_records = []

    while True:
        print("=== Student Record Management System ===")
        print("1. Add Student Record (Insert)")
        print("2. Search Student Record")
        print("3. Delete Student Record")
        print("4. Display All Records")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ").strip()
        print()

        if choice == "1":
            add_student(student_records)
        elif choice == "2":
            search_student(student_records)
        elif choice == "3":
            delete_student(student_records)
        elif choice == "4":
            display_all(student_records)
        elif choice == "5":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.\n")


if __name__ == "__main__":
    main()
