import collections
from collections import Counter

c = Counter('gallad')
print(c)

c = Counter(['a', 'a', 'b', 'c', 'c'])
print(c)

c = Counter({'a':1, 'b':2})
print(c)

c = Counter(cats=4, dogs=7)
print(c)
print(c['cats'])

print(list(c.elements()))

print(c.most_common(2))

c = Counter(a=4, b=2, c=0, d=-2)
d = ['a', 'b', 'b', 'c']



# c.subtract(d)
# print(c)
# c.update(d)
# print(c)
# c.clear()
# print(c)

# VI. 09:53











