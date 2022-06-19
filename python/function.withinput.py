# Simple function
def greet():
    print("Hello")
    print("how do you do?")
    print("Isn't the weather nice today?")

greet()

# Function that allows for input

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"how do you do {name}?")
    
greet_with_name("Csaba")

# The Parameter (name) is the name of the data that's being passed in
# The Argument (Csaba) is the actual value of the data.