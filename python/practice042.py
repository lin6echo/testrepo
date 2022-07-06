thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y) 
print(thistuple)

thistuple1 = ("apple", "banana", "kiwi")
y = ("orange",)
thistuple1 += y
print(thistuple1)