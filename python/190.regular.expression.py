import re

def multi_re_find(pattern, phrase):
    
    for pat in pattern:
        print("Searching for pattern {}".format(pat))
        print(re.findall(pat, phrase))
        print('\n')
        
test_phrase = 'This is a string! But it has punctuation. How can we remove it?'
test_patterns = ['[^!.?]+']

multi_re_find(test_patterns, test_phrase)

test_patterns = ['[a-z]+']

multi_re_find(test_patterns, test_phrase)

test_patterns = ['[A-Z]+']

multi_re_find(test_patterns, test_phrase)

test_phrase = 'This is a string with numbers 123321 and a symbol #hashtag '

test_patterns = [r'\d+']

multi_re_find(test_patterns, test_phrase)

test_patterns = [r'\D+']

multi_re_find(test_patterns, test_phrase)

test_patterns = [r'\s+']

multi_re_find(test_patterns, test_phrase)

test_patterns = [r'\S+']

multi_re_find(test_patterns, test_phrase)

test_patterns = [r'\w+']

multi_re_find(test_patterns, test_phrase)

test_patterns = [r'\W+']

multi_re_find(test_patterns, test_phrase)










