def factorial(x):
    if x == 1:
        return 1
    else:
        return (x * factorial(x - 1))
    
num = 4
print(num, factorial(num))  # 1 x 2 x 3 x 4 = 24