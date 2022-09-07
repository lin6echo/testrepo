# INHERITANCE
class Animal():
    
    def __init__(self):
        print("ANIMAL CREATED")
        
    def whoAmI(self):
        print("ANIMAL")
        
    def eat(self):
        print("EATING")
        
class Dog(Animal):                          # Inherit
    
    def __init__(self):
       Animal.__init__(self)
       print("DOG CREATED")
       
    def bark(self):
        print("WOOF")
        
    def eat(self):
        print("DOG EATING")                 # Overwrite eat
       
mydog = Dog()
mydog.whoAmI()
mydog.eat()
mydog.bark()
    
        
# myA = Animal()
# myA.whoAmI()
# myA.eat()