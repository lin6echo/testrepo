# itertools: product, permutation, combinations, accumulate, groupby, and infinite iterators
from itertools import product
a = [1, 2]
b = [3]
prod = product(a,b, repeat=2)
print(list(prod))
#.......................................
from itertools import permutations
a = [1, 2, 3]
perm = permutations(a)
print(list(perm))

a = [1, 2, 3]
perm = permutations(a, 2)
print(list(perm))
#........................................
from itertools import combinations, combinations_with_replacement
a = [1, 2, 3, 4]
comb = combinations(a, 2)
print(list(comb))
comb_wr = combinations_with_replacement(a, 2) 
print(list(comb_wr))
#.........................................
from itertools import accumulate
import operator
a = [1, 2, 3, 4]
acc = accumulate(a, func=operator.mul)
print(a)
print(list(acc))

a = [1, 2, 3, 4]
acc = accumulate(a, func=max)
print(a)
print(list(acc))
#...........................................
from itertools import groupby

def smaller_than_3(x):
    return x < 3

a = [1, 2, 3, 4]
group_obj = groupby(a, key=smaller_than_3)
for key, value in group_obj:
    print(key, list(value))
    
def smaller_than_3(x):
    return x < 3

a = [1, 2, 3, 4]
group_obj = groupby(a, key=lambda x: x<3)
for key, value in group_obj:
    print(key, list(value))
#...............................................
persons = [{"name" : "Tim", "age" : 25}, {"name" : "Dan", "age" : 25}, 
           {"name" : "Lisa", "age" : 27}, {"name" : "Claire", "age" : 28}]

group_obj = groupby(persons, lambda x: x["age"])
for key, value in group_obj:
    print(key, list(value))
#...............................................
from itertools import count, cycle, repeat

for i in count(10):
    print(i)
    if i == 15:
        break
    
# a = [1, 2, 3]
# for i in cycle(a):        # infinite loop
#     print(i)

a = [1, 2, 3]
for i in repeat(1, 4):        
    print(i)








