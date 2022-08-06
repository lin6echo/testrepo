# IMPORTING
    # Some modules are pre-installed with python e.g. random/datetime.
    # Other modules need to be installed from pypi.org
import random
n = random.randint(3, 10)
print(n)

# ALIASING
    # You can use the as keyword to give your module a different name.
import random as r
n = r.randint(1, 5)
print(n)

# IMPORTING FROM MODULES
    # You can import a specific thing from a module. e.g. a function/constant. You do this with the from keyword.
    # It can save you from having to type the same thing many times.
from random import randint
n = randint(1, 5)
print(n)

# IMPORTING EVERYTHING
    # You can use the wildcard(*) to import everything from a module. Beware, this usually reduces code readability.
from random import *
list = [1, 2, 3]
choice(list)
# More readable/understood
random.choice(list)