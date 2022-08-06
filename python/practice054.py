# The range() Function
for x in range(6):
    print(x)

for x in range(2,7):
    print(x)

# Else in For Loop
for x in range(6):
    print(x)
else:
    print("Finally finished")

for x in range(6):
    if x == 3: break
    print(x)
else:
    print("Finally finished!")

# Nested Loops
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
    for y in fruits:
        print(x, y)