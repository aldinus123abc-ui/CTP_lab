import xml.etree.ElementTree as ET

def modify_xml(filename, name, deparment, cgp):
    tree = ET.parse(filename)
    root = tree.getroot()

    for student in root.findall("student"):
        if student.find("name").text == name:
            student.find("department").text = deparment
            student.find("gpa").text = cgp

    new_student = ET.SubElement(root, "student", id="103")
    ET.SubElement(new_student, "name").text = "Charlie"
    ET.SubElement(new_student, "department").text = "Mechanical Engg"
    ET.SubElement(new_student, "gpa").text = "3.9"
    print("Added new student: Charlie")

    ET.indent(tree, space="  ")
    tree.write("stuco,[dents_updated.xml", encoding="utf-8", xml_declaration=True)
    print("Saved modified XML to students_updated.xml\n")

name = input("Enter the name of the person which you want to update: ")
department = input("Enter the updated department: ")
cg = input("Enter the updated gpa: ")
modify_xml("students.xml", name, department, cg)

with open("students_updated.xml", "r") as f:
    print(f.read())