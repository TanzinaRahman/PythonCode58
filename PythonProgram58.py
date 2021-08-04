# Constructor


class Student:
    roll = ""
    gpa = ""

    def __init__(self, roll, gpa):
        self.roll = roll
        self.gpa = gpa

    def display(self):
        print(f"Roll : {self.roll}, GPA : {self.gpa}")


rahim = Student(101, 3.70)
rahim.display()


karim = Student(102, 3.60)
karim.display()
