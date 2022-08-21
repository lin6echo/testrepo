def func(x):
    return x + 5

func2 = lambda x: x + 5
func3 = lambda x: x * 3

print(func2(9))
print(func(2))
print(func3(3))

# V. 02:09

def func(x):
    func2 = lambda x: x + 5
    return func2(x) + 77
print(func(2))

func3 = lambda x,y: x + y
print(func3(3,4))

# V. 03:59

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

newlist = list(map(lambda x: x + 5, a))
print(newlist)

newlist = list(filter(lambda x: x%2 == 0, a))
print(newlist)




