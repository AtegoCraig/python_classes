class Student:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        return f"My name is {self.name} and I am {self.age} years old."

    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}, Course: {self.course}"
    
    def role(self):
        return "I am a student"

class GraduateStudent(Student):
    def role(self):
        return "I am a graduate student"

class TeachingAssistant(GraduateStudent):
    def role(self):
        return "I assist with teaching"

s1 = Student("John")
s2 = GraduateStudent("Jane")
s3 = TeachingAssistant("Emily")

for s in (s1, s2, s3):
    print(f"{s.name}: {s.role()}")