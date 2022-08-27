class Person:
    "This is a person class"
    age = 10

    def greet(self):
        print('Hello')


# Output: 10
print(Person.age)

csaba = Person()
# Output: <function Person.greet>
print(Person.greet)

# Output: "This is a person class"
print(Person.__doc__)

csaba.greet()