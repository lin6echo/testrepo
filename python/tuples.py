mytuple = ("Max", 28, "Boston")
print(mytuple)
#.................................................
mytuple = tuple(["Max", 28, "Boston"])
print(mytuple)
#..................................................
item = mytuple[1]
print(item)
#...................................................
for i in mytuple:
    print(i)
#................................................    
if "Max" in mytuple:
    print("yes")
else:
    print("no")
#...............................................
my_tuple = ('a', 'p', 'p', 'l', 'e')

print(len(my_tuple))
print(my_tuple.count('p'))
print(my_tuple.index("p"))

my_list = list(my_tuple)
print(my_list)

my_tuple2 = tuple(my_list)
print(my_tuple2)
#................................................
a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
b = a[2:5]
print(b)

b = a[::3]
print(b)
#..................................................
mytuple = ("Max", 28, "Boston")

name, age, city = mytuple
print(name)
print(age)
print(city)