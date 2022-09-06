def hello(name = "Csaba"):
    return "hello " + name

print(hello())

newgreet = hello
print(newgreet())