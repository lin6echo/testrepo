mydict = {"name" : "Csaba", "wife": "Szilvia", "firstchild": "Zsani", "secondchild": "Bogi" }
print(mydict)

try:
    print(mydict["name"])
    print(mydict["lastname"])
    
except:
    print("ERROR")