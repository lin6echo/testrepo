import sys

mygenerator = (i for i in range(10) if i % 2 == 0)
for i in mygenerator:
    print(i)
    
mylist = [i for i in range(1000000) if i % 2 == 0]
# print(mylist)
print(sys.getsizeof(mylist))
    
mygenerator = (i for i in range(1000000) if i % 2 == 0)
#print(list(mygenerator))
print(sys.getsizeof(mygenerator))
    
    
    