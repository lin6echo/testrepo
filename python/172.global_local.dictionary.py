s = "GLOBAL VARIABLES"

def func():
    mylocal = 10
    print(locals())
    
func()                                      # return: {'mylocal': 10}

def func():
    mylocal = 10
    print(globals()['s'])
    
func()                                      # return: GLOBAL VARIABLES