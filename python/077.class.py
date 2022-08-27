class Person:
      def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

x = Student("Mike", "Olsen", 2019)
print(x.graduationyear)

class Person:
      def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

        def printname(self):
            print(self.firstname, self.lastname)

class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Mike", "Olsen", 2019)
x.welcome()

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)
print(next(myit))

mystr = "banana"
myit = iter(mystr)

print(next(myit))

mytuple = ("apple", "banana", "cherry")

for x in mytuple:
    print(x)

mystr = "banana"

for x in mystr:
    print(x)