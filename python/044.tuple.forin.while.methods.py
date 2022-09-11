thistuple = ("apple", "orange", "kiwi")
for x in thistuple:
    print(x)

thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
    print(thistuple[i])

thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
    print(thistuple[i])
    i = i + 1

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)

thistuple1 = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple1.count(5)
print(x)                                        # count() method returns the number of times a specified value appears in the tuple

thistuple2 = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple2.index(8)
print(x)                                        # Tuple index() method - Search for the first occurrence of the value 8, and return its position: