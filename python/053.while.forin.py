# The while Loop
i = 1
while i < 6:
    print(i)
    i += 1

# The break Statement
a = 1
while a < 6:
    print(a)
    if a == 3:
        break
    a += 1

# The continue Statement
b = 0
while b < 6:
    b += 1
    if b == 3:
        continue
    print(b)

# The else Statement
c = 1
while c < 6:
    print(c)
    c += 1
else:
    print("c is no longer less than 6")

# Python For Loops
fruits = ["apple", "banana", "cherry"]
print(type(fruits))
for x in fruits:
    print(x)

# Looping Through a String
for x in "banana":
    print(x)

# The break Statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)

# The continue Statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)