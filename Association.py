class Teacher:
    def __init__(self,name):
        self.name = name
    def teach(self):
        print(f"{self.name} is teaching")
class Student:
    def __init__(self,name):
        self.name = name
    def learn_from(self,teacher):
        print(f"{self.name} is learning from {teacher.name}")

teacher = Teacher("Rahul Sir")
student = Student("Aman")
student.learn_from(teacher)