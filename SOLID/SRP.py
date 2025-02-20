class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

class StudentRepository:
    def save_to_db(self, student):
        print(f"Saving {student.name} (Roll: {student.roll}) to database")

class StudentDisplay:
    def show(self, student):
        print(f"Student Name: {student.name}, Roll: {student.roll}")


student = Student("John Doe", 101)
# print(student)
repo = StudentRepository()
display = StudentDisplay()

repo.save_to_db(student)
display.show(student)

# bad practice
# student = Student("John Doe", 101)
# student.save_to_db()  # ⚠ Bad practice
# student.display()  # ⚠ Bad practice

