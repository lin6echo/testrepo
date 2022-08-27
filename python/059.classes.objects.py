# Python Classes/Objects

# Create a Class
class MyClass:
    x = 5

# Create Object
p1 = MyClass()
print(p1.x)

# The __init__() Function
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = Person("John", 36)
print(p1.name)
print(p1.age)

