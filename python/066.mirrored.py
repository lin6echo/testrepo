from unicodedata import mirrored

i = 0
a = 'abrakadabra'
lst = list(a)
x = int(len(lst)/2)

for i in range(x):
    
    if lst[i] == lst[len(lst)-1-i]:
        print("Same")
    else:
        
        print("Not Same")
        print("unmirrored")
        exit() 
print("mirrored")