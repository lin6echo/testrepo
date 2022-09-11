import re

patterns = ['term1', 'term2']

text = 'This is a string with term1, not the other!'

for pattern in patterns:
    print("I'm searching for: " + pattern )
    
    if re.search(pattern, text):
        print("MATCH!")
        
    else:
        print("NO MATCH!")


