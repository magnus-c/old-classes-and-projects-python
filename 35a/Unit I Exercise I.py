'''
Magnus Chiu
CIS 41A Spring 2022
Unit I Exercise I
'''
import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
        
    def getArea(self):
        area = math.pi * self.radius ** 2
        return area
    
class Cylinder(Circle):
    def __init__(self, radius, height):
        Circle.__init__(self, radius)
        self.height = height
        
    def getVolume(self):
        volume = Circle.getArea(self.radius) * self.height
        return volume
        
c1 = Circle(4)
print("Circle area is:",round(c1.getArea(),2))
c2 = Cylinder(Circle(2), 5)
print("Cylinder volume is:",round(c2.getVolume(),2))
        
'''
Execution Results:
Circle area is: 50.27
Cylinder volume is: 62.83
'''