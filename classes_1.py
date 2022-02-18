
# A class of a student who receives values
# and also some functions

class Student:
    def __init__(self, max_grades=3):
        self.name = ""
        self.id = 0
        self.grades = []
        self.max_grades = max_grades

    def print_data(self):
        print(f'Name: {self.name}, ID: {self.id}, Grades: {self.grades}')

    def add_grade(self, grade):
        if len(self.grades) < self.max_grades:
            self.grades.append(grade)

    def get_avg(self):
        avg = sum(self.grades) / len(self.grades)
        return avg

# An example of running a program
s = Student(3)
s.name = "Roe"
s.id = 123
s.add_grade(80)
s.add_grade(90)
s.add_grade(100)
s.print_data()
print(s.get_avg())
s.add_grade(70)
print(s.get_avg())

