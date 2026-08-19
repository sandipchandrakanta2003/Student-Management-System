class Student:

    def __init__(self, sid, name, course):
        self.sid = sid
        self.name = name
        self.course = course

    def __str__(self):
        return f"{self.sid},{self.name},{self.course}"