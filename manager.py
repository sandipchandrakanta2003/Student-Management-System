from student import Student
from file_handler import save_student, get_students

def add_student():
    try:
        sid = input("Student ID: ")
        name = input("Name: ")
        age = input("Age: ")
        course = input("Course: ")

        student = Student(sid, name, age, course)
        save_student(student)

        print("Student Added Successfully")

    except Exception as e:
        print("Error:", e)


def view_students():
    students = get_students()

    if not students:
        print("No Students Found")
        return

    print("\nStudent Records")
    print("-" * 50)

    for student in students:
        print(student.strip())


def search_student():
    sid = input("Enter Student ID: ")

    students = get_students()

    for student in students:
        data = student.strip().split(",")

        if data[0] == sid:
            print("\nStudent Found")
            print(student)
            return

    print("Student Not Found")


def delete_student():
    sid = input("Enter Student ID to Delete: ")

    students = get_students()

    with open("students.txt", "w") as file:

        for student in students:
            data = student.strip().split(",")

            if data[0] != sid:
                file.write(student)

    print("Student Deleted Successfully")


def update_student():
    sid = input("Enter Student ID to Update: ")

    students = get_students()

    updated_data = []

    found = False

    for student in students:

        data = student.strip().split(",")

        if data[0] == sid:

            found = True

            name = input("New Name: ")
            age = input("New Age: ")
            course = input("New Course: ")

            updated_data.append(
                f"{sid},{name},{age},{course}\n"
            )

        else:
            updated_data.append(student)

    with open("students.txt", "w") as file:
        file.writelines(updated_data)

    if found:
        print("Student Updated Successfully")
    else:
        print("Student Not Found")