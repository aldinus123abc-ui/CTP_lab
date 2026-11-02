def calculate_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


def process_student_marks(input_filename, output_filename):
    try:
        with open(input_filename, "r") as infile:
            lines = infile.readlines()

        processed_data = []

        for line in lines:
            if not line.strip():
                continue

            parts = [part.strip() for part in line.split(",")]
            name = parts[0]

            marks = [float(mark) for mark in parts[1:]]


            total_marks = sum(marks)
            average_marks = total_marks / len(marks) if marks else 0
            grade = calculate_grade(average_marks)

            processed_data.append(
                f"Name: {name} | Marks: {marks} | Total: {total_marks:.2f} | Average: {average_marks:.2f} | Grade: {grade}\n"
            )

        with open(output_filename, "w") as outfile:
            outfile.writelines(processed_data)

        print(
            f"Successfully processed {len(processed_data)} student records. Results saved to '{output_filename}'."
        )

    except FileNotFoundError:
        print(
            f"Error: The file '{input_filename}' was not found. Please check the file path."
        )
    except Exception as e:
        print(f"An unexpected error occurred: {e}")




input_file = "students.txt"
output_file = "student_results.txt"

process_student_marks(input_file, output_file)