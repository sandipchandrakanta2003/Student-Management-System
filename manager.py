from student import Student
from file_handler import save_student, load_students

class StudentManager:

    def add_student(self, sid, name, course):
        student = Student(sid, name, course)
        save_student(student)

    def get_all_students(self):
        return load_students()