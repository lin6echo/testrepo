thistuple = ("apple", "banana", "kiwi")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)

fruits = ("apple", "orange", "melon")
(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)