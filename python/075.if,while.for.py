
a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are True.")

a = 200
b = 33
c = 500
if a > b or a > c:
    print("At least one of the conditions is True.")

x = 41
if x > 10:
    print("Above ten,")
if x > 20:
    print("and also above 20!")
else:
    print("but not above 50.") 

i = 1
while i < 6:
    print(i)
    i += 1

i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

fruits = ["banana", "apple", "cherry"]
for x in "banana":
    print(x)

for x in range(2,6):
    print(x)

for x in range(6):
    print(x)
else:
    print("Finally finished!")

for x in range(6):
    if x == 3: break
    print(x)
else:
    print("Finally finished!")