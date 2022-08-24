thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y) 
print(thistuple)

thistuple1 = ("apple", "banana", "kiwi")
y = ("orange",)
thistuple1 += y
print(thistuple1)

thistuple = ("apple", "banana", "kiwi")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)

thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
    print(thistuple[i])

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)

thisset6 = {"apple", "banana", "cherry"}
myset = ["kiwi", "orange"]
thisset6.update(myset)
print(thisset6)

tuple = ("apple", "banana", "kiwi", "orange", "mango", "pear")
print(tuple)
print(len(tuple))
print(type(tuple))
print(tuple[1])
print(tuple[1:5])

thistuple = ("apple", "banana", "cherry")

for x in thistuple:
    print(x)

for i in range(len(thistuple)):
    print(thistuple[i])

i = 0
while i < len(thistuple):
    print(thistuple[i])
    i = i + 1
