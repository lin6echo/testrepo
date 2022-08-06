class MyNumbers:
        def __iter__(self):
            self.a = 1
            return self

        def __next__(self):
            x = self.a
            self.a += 1
            return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)
    
def myfunc():
    x = 300
    print(x)

myfunc()

def myfunc():
    x = 300
    def myinnerfunc():
        print(x)
    myinnerfunc()

myfunc()

x = 300

def myfunc():
    x = 200
    print(x)

myfunc()

print(x)