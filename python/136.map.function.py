li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def func(x):
    return x ** x

newlist = []
for x in li:
    newlist.append(func(x))

print(newlist)

li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def func(x):
    return x ** x

print(list(map(func, li)))
print([func(x) for x in li if x % 2 == 0])

def addition(n):
    return n + n
  
# We double all numbers using map()
numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))

# III/ 03:51