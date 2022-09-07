mylist = [1, 2, 3]
mylist.append(4)
print(mylist)

class Dog(): 
    def __init__(self, breed, name):
        self.breed = breed
        self.name = name
      
mydog = Dog("Labrador","Astor")
#otherdog = Dog(breed = "Huskie")
print(mydog.breed)
print(mydog.name)
#print(otherdog.breed)

class Dog():
    
    # CLASS OBJECT ATTRIBUTE
    species = "Mammal"
    
    def __init__(self, breed, name):
        self.breed = breed
        self.name = name
      
mydog = Dog("Labrador","Astor")
#otherdog = Dog(breed = "Huskie")
print(mydog.breed)
print(mydog.name)
print(mydog.species)
#print(otherdog.breed)



    