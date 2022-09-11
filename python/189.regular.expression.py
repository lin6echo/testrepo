import re

def multi_re_find(pattern, phrase):
    
    for pat in pattern:
        print("Searching for pattern {}".format(pat))
        print(re.findall(pat, phrase))
        print('\n')
        
test_phrase = 'sdsd.....sssddd........sdddsdddd.........dsds.....dssssssss........sdddddddddd'
test_patterns = ['sd*']

multi_re_find(test_patterns, test_phrase)

test_patterns = ['sd+']

multi_re_find(test_patterns, test_phrase)

test_patterns = ['sd?']

multi_re_find(test_patterns, test_phrase)

test_patterns = ['sd{3}']

multi_re_find(test_patterns, test_phrase)

test_patterns = ['sd{2,3}']

multi_re_find(test_patterns, test_phrase)








