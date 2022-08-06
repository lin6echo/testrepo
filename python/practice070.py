tuple = ("apple", "banana", "kiwi", "orange", "mango", "pear")
print(tuple)
print(len(tuple))
print(type(tuple))
print(tuple[1])
print(tuple[1:5])


# While loop
n = 1
while n < 100:
    n += 1
    print(n)

# For loop
all_fruits = ["apple", "banana", "kiwi"]
for fruit in all_fruits:
    print(fruit)

thistuple1 = ("apple", "banana", "cherry")
if "banana" in thistuple1:
    print("Yes")

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)
