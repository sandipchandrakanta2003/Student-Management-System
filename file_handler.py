FILE_NAME = "students.txt"

def save_student(student):
    with open(FILE_NAME, "a") as file:
        file.write(str(student) + "\n")

def get_students():
    try:
        with open(FILE_NAME, "r") as file:
            return file.readlines()
    except FileNotFoundError:
        return []