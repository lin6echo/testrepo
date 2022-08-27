if 5 > 2:
    print("Five bigger than 2")

# Creating variables
a = 5
b = "Csaba"
print(a)
print(b)

x = int(3)
z = str(3)
y = float(3)
print(x, z, y)
print(type(x))
print(type(z))
print(type(y))


x, y, z = ("Orange", "Banana", "Pear")
print(x, y, z)

fruits = ["Orange", "Banana", "Pear"] # Unpacking a collection
x, y, z = fruits
print(x, y, z)