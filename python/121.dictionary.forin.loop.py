dict = {"csaba": 1, "sziszi": 2, "lili": 3}
# print all key name
for x in dict:
    print(x)
    
# another way
for x in dict.keys():
    print(x)
    
# print all values name
for x in dict:
    print(dict[x])
    
# another way
for x in dict.values():
    print(x)
    
# keys and values
for x, y in dict.items():
    print(x, y)