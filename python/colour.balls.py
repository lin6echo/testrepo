green = [1,2,3,4,5]
red = [6,7,8,9,10]
blue = [11,12,13,14,15]
yellow = [16,17,18,19,20]
print(green)
print(type(green))

import random

randomlist = random.sample(range(1, 21), 5)
print(randomlist)

import numpy as np

outcome = np.random.randint(1, 21, size=10)
print(outcome)

randomlist = []

for i in range(0,5):
        n = random.randint(1, 21)
        randomlist.append(n)
        print(randomlist)


# if x <= 5:
#      print("green")
# elif x > 5 and x <= 10:
#      print("red")
# elif x > 10 and x <= 15:
#      print("blue")
# else:
#      print("yellow")
