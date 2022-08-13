myset = {1, 2, 3}
print(myset)

myset = set([1, 2, 3])
print(myset)
#................................................
myset = {"Hello"}
print(myset)
myset = set("Hello")
print(myset)
#...................................................
myset = set()

myset.add(1)
myset.add(2)
myset.add(3)

print(myset)
#..................................................
myset = set()

myset.add(1)
myset.add(2)
myset.add(3)

myset.remove(3)
print(myset)
#..................................................
myset = set()

myset.add(1)
myset.add(2)
myset.add(3)

myset.discard(3)
print(myset)
#..................................................
myset = {1, 2, 3}
myset.clear()
print(myset)
#...................................................
myset = {1, 2, 3}
myset.pop()
print(myset)
#..................................................
myset = {1, 2, 3}
for i in myset:
    print(i)
#..................................................
myset = {1, 2, 3}
if 4 in myset:
    print(myset)
else:
    print("error")
#...................................................
odds = {1,3,5,7}
even = {2,4,6,8}
primes = {2,3,5,7}

u = odds.union(even)
print(u)

i = odds.intersection(primes)
print(i)
    
j = even.intersection(primes)
print(j)
#.....................................................
setA = {1,2,3,4,5,6,7,8,9}
setB = {1,2,3,10,11,12}

diff = setA.difference(setB)
print(diff)

diff = setB.difference(setA)
print(diff)
diff = setB.symmetric_difference(setA)
print(diff)
#....................................................
setA = {1,2,3,4,5,6,7,8,9}
setB = {1,2,3,10,11,12}

setA.update(setB)
print(setA)

setA.intersection(setB)
print(setA)
#....................................................
setA = {1,2,3,4,5,6,7,8,9}
setB = {1,2,3,10,11,12}

setA.intersection_update(setB)
print(setA)
#....................................................
setA = {1,2,3,4,5,6,7,8,9}
setB = {1,2,3,10,11,12}

setA.difference_update(setB)
print(setA)
#....................................................
setA = {1,2,3,4,5,6,7,8,9}
setB = {1,2,3,10,11,12}

setA.symmetric_difference_update(setB)
print(setA)
#....................................................
setA = {1,2,3,4,5,6}
setB = {1,2,3}

print(setA.issubset(setB))
print(setB.issubset(setA))

print(setA.issuperset(setB))
print(setB.issuperset(setA))
#...................................................
setA = {1,2,3,4,5,6}
setB = {1,2,3}
setC = {7,8}

print(setA.isdisjoint(setB))
print(setB.isdisjoint(setA))
print(setB.isdisjoint(setC))
#...................................................
setA = {1,2,3,4,5,6}

setB = setA
setB.add(7)

print(setA)
print(setB)
#.....................................................
setA = {1,2,3,4,5,6}

setB = setA.copy()
setB.add(7)

print(setA)
print(setB)
#.......................................................
setA = {1,2,3,4,5,6}

setB = set(setA)
setB.add(7)

print(setA)
print(setB)
#........................................................
a = frozenset([1,2,3,4,5]) # immutable

a.add(6)        # attribute error
a.remove(1)     # attribute error


























