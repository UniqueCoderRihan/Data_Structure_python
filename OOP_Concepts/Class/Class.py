class Student:
    def __init__(self,roll,subject):
        self.roll = roll
        self.subject = subject

    def details(self):
        print(self.roll)

Student1 = Student(789122,"CSE")
print(Student1.details())

