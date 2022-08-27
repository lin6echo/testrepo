# word = 'Sample1'
# lst = []
# for i in word:
#      lst.append(i)

# print(lst)

#from unicodedata import mirrored


i = 0
a = 'abara'
lst = list(a)
x = int(len(lst)/2)
csingilingi = True

for i in range(x):
    
    if lst[i] == lst[len(lst)-1-i]:
        
        print("Same")
    else:
        csingilingi = False
        print("Not Same")
        print("unmirrored")
        break
if csingilingi:
    print("mirrored")

    
        



# if lst[0] == lst[-1] and lst[1] == lst[-2]:
#     print("Same")
# else:
#      print("Not same")


#while lst[0] == lst[-1]:
# while i < len(a):
#     if a[i] == a[-i]:
#         i += 1
#     print(True)
# else:
#     print(False)

# i = 0, -1

# while i < len(a)
    