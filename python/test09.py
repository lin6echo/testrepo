from unittest import result


def stringBit(mystring):
    result = ""
    
    for i in range(len(mystring)):
        if i%2 == 0:
            result = result + mystring[i]
    
    return result
