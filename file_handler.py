FILE_NAME = "students.txt"

def save_student(student):
    with open(FILE_NAME, "a") as file:
        file.write(str(student) + "\n")

def load_students():
    students = []

    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                students.append(line.strip().split(","))

    except FileNotFoundError:
        pass

    return students