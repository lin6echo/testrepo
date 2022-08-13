# collections: counter, namedtuple, OrderedDict, defaultdict, deque
from collections import Counter
a = "aaaaaabbbbbbcccccc"
my_counter = Counter(a)
print(my_counter.items())

a = "aaaaaabbbbbbcccccc"
my_counter = Counter(a)
print(my_counter.values())

a = "aaaaaabbbbbbcccccc"
my_counter = Counter(a)
print(my_counter.keys())

a = "aaaaaabbbbbbcccccc"
my_counter = Counter(a)
print(my_counter)
print(my_counter.most_common(1))

a = "aaaaaabbbbbbcccccc"
my_counter = Counter(a)
print(my_counter)
print(list(my_counter.elements()))
#..............................................
from collections import namedtuple

Point = namedtuple("Point", "x,y")
pt = Point(1, -4)
print(pt)

Point = namedtuple("Point", "x,y")
pt = Point(1, -4)
print(pt.x, pt.y)
#..............................................
from collections import OrderedDict
ordered_dict = {}
ordered_dict["a"] = 1
ordered_dict["b"] = 2
ordered_dict["c"] = 3
ordered_dict["d"] = 4
print(ordered_dict)
#.............................................
from collections import defaultdict
d = defaultdict(int)
d["a"] = 1
d["b"] = 2
print(d)
print(d["a"])
#.............................................
from collections import deque
d = deque()

d.append(1)
d.append(2)

d.appendleft(3)
print(d)

d.popleft()
print(d)

# d.clear()
# print(d)

d.extendleft([4,5,6])
print(d)

d.rotate(1)
print(d)














