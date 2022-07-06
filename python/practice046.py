# You can loop through the set items by using a for loop:

thisset0 = {"apple", "banana", "kiwi"}
for x in thisset0:
    print(x)

set1 = {"apple", "banana", "kiwi"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)                             # the union() method that returns a new set containing all items from both sets

set4 = {"apple", "banana", "kiwi"}
set5 = {1, 2, 3}
set4.update(set5)
print(set4)                             # the update() method that inserts all the items from one set into another

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)                                # The intersection_update() method will keep only the items that are present in both sets.

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)                                # The intersection() method will return a new set, that only contains the items that are present in both sets.


x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)                                # The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)                                # The symmetric_difference() method will return a new set, that contains only the elements that are NOT present in both sets.

