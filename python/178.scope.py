# local
lambda x: x**2

# enclosing function locals
name = "This is a global name!"

def greet():
    name = "Csaba"
    
    def hello():
        print("Hello " + name)
        
    hello()
        
greet()
print(name)
