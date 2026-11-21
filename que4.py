def display_students(title, student_set):
    print(f"\n--- {title} ({len(student_set)}) ---")
    if not student_set:
        print("None")
        return

    print(f"{'Roll No':<12} {'Name':<20} {'Branch':<10}")
    print("-" * 44)
    for roll_no, name, branch in sorted(student_set):
        print(f"{roll_no:<12} {name:<20} {branch:<10}")


def analyse_enrolments():
    s1 = ("CS101", "Aarav Sharma", "CSE")
    s2 = ("CS102", "Diya Patel", "CSE")
    s3 = ("EC201", "Rohan Verma", "ECE")
    s4 = ("CS103", "Ananya Nair", "CSE")
    s5 = ("ME301", "Kabir Das", "MECH")
    s6 = ("EC202", "Meera Iyer", "ECE")

    python_course = {s1, s2, s3, s4}
    data_science_course = {s2, s4, s5, s6}

    display_students("Enrolled in Python Programming", python_course)
    display_students("Enrolled in Data Science", data_science_course)

    all_enrolled = python_course.union(data_science_course)
    display_students("1. Union: All Unique Students (Python OR Data Science)", all_enrolled)

    common_students = python_course.intersection(data_science_course)
    display_students("2. Intersection: Common Students (Python AND Data Science)", common_students)

    only_python = python_course.difference(data_science_course)
    display_students("3. Difference: Unique to Python Only", only_python)

    only_data_science = data_science_course.difference(python_course)
    display_students("4. Difference: Unique to Data Science Only", only_data_science)

    single_course_only = python_course.symmetric_difference(data_science_course)
    display_students("5. Symmetric Difference: Enrolled in Exactly One Course", single_course_only)


if __name__ == "__main__":
    analyse_enrolments()
