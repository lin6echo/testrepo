def add7(x):
    return x + 7

def isOdd(x):
    return x % 2 != 0

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

b = list(filter(isOdd, a))
print(b)                                        # return: [1, 3, 5, 7, 9]

c = list(map(add7, b))
print(c)                                        # return: [8, 10, 12, 14, 16]

# ---------------------------------------------------------------------------------------

def add7(x):
    return x + 7 

def isEven(x):
    return x % 2 == 0

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

b = list(filter(isEven, a))
print(b)                                        # return: [2, 4, 6, 8, 10]

c = list(map(add7, b))
print(c)                                        # return: [9, 11, 13, 15, 17]