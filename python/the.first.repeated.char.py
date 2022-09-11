def firstRepeatedChar(str):
    x = {}
    for char in str:
        if char in x:
            return char
        else: 
            x[char] = 0
            
    return ''
print(firstRepeatedChar("STARWARS"))
        