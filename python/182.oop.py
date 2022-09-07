class Circle():
    
    pi = 3.14
    
    def __init__(self, radius = 1):
        self.radius = radius
        
    def area(self):
        return self.radius * self.radius * Circle.pi
    
    def set_radius(self, new_r):
        self.radius = new_r
        
        
myc = Circle(3)

print(myc.radius)
print(myc.area())

myc.radius = 100
print(myc.area())

myc.set_radius(1000)
print(myc.area())
