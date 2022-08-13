def mygenerator():
    yield 1
    yield 2
    yield 3
    
g = mygenerator()

#print(sum(g))

print(sorted(g))