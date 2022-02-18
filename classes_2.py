
# Continued from the previous file,
# here I create a school class that accepts all students,
# and at the end returns all their data

from classes_1 import Student

class School():
    def __init__(self):
        self.students = []

    def add_sdudent(self, s):
        arr = list(filter(lambda x: x.id == s.id, self.students))
        if len(arr) == 0:
            self.students.append(s)
        else:
            print("This student already exists")

    def print_students_data(self):
        for s in self.students:
            s.print_data()


# Function for finding a particular student in a school,
# by ID card
def find_in_school(sc, id):
    arr = list(filter(lambda x : x.id == id ,sc.students))
    if len(arr) > 0:
        print(arr[0].name)
    else:
        print("Not exist")
        

# An example of running a program
s1 = Student()
s1.name = "Dan"
s1.id = 1234
s1.grades = [90, 85]
s1.add_grade(100)

s2 = Student(2)
s2.name = "Rut"
s2.id = 4567
s2.grades = [92, 75]
s2.add_grade(99)

s3 = Student(4)
s3.name = "Avi"
s3.id = 3579
s3.grades = [90, 80, 79]
s3.add_grade(100)

# Python does not add student number 4
# because his ID already exists on the list
s4 = Student()
s4.name = ""
s4.id = 1234
s4.grades = [98, 77]
s4.add_grade(94)

sc = School()
sc.add_sdudent(s1)
sc.add_sdudent(s2)
sc.add_sdudent(s3)
sc.add_sdudent(s4)

sc.print_students_data()

find_in_school(sc, 1234)
find_in_school(sc, 8765)

