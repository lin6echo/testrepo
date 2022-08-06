# CREATING A PYTHON CLASS
    # You create a class using the class keyword.
    # Note, cladd names in Python are PascalCased. So to create an empty class []
class Myclass:[] # define class

# CREATING AN OBJECT FROM A CLASS
    # You can create a new instance of an object by using the class name +()
class Car:
    pass
my_toyota = Car()

# CLASS METHODS
    # You can create a function that belongs to a class, this is known as a method.
class Car:
    def drive(self):
        print("move")
my_honda = Car()
my_honda.drive()

# CLASS VARIABLES
    # You can create a variable in a class. The value of the variable will be available to all objects created from the class.
class Car:
    colour = "black"
car1 = Car()
print(car1.colour) 

# THE _INIT_METHOD
    # The init method is called every time a new object is created from the class.

class Car:
    def __init__(self):
        print("Building car")
my_toyota = Car()


# CLASS PROPERTIES
    # You can create a variable in the init() of a class so that all objects created from the class has access to that variable.
class Car:
    def __init__(self, name):
        self.name ="Jimmy"

# CLASS INHERITANCE
    # When you create a new class, you can inherit the methods and properties of another class.
class Animal:
    def breathe(self):
        print("breathing")
class Fish(Animal):
    def breathe(self):
        super().breathe()
        print("underwater")
nemo = Fish()
nemo.breathe()
