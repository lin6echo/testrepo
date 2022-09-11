import re

text = 'This is a string with term1, not the other!'

match = re.search('term1', text)

print(match.start())