x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

import random

skandi = list(range(1,35))
random.shuffle(skandi)
seven_nums = skandi[:7]
print(seven_nums)    

hatos = list(range(1,45))
random.shuffle(hatos)
six_nums = hatos[:6]
print(six_nums)    