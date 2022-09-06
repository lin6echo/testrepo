def hello(name = "Csaba"):
    print("THE HELLO() FUNCTION HAS BEEN RUN!")
    def greet():
        return "THIS STRING INSIDE GREET()!"
    def welcome():
        return "THIS STRING INSIDE WELCOME()!"
    
    if name == "Csaba":
        return greet
    else:
        return welcome
x = hello()
print(x())  
    
    
    
def hello(name = "Csaba"):
    print("THE HELLO() FUNCTION HAS BEEN RUN!")
    def greet():
        return "THIS STRING INSIDE GREET()!"
    def welcome():
        return "THIS STRING INSIDE WELCOME()!"
    print(greet())
    print(welcome())
    print("End of hello()!")
hello()