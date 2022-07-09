# Create a Parent Class
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
def printname(self):
    print(self.firstname, self.lastname)

# Create a Child Class
class Student(Person):
    pass

x = Student("Mike", "Olsen")
x.printname()