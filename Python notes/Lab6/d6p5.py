from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, l, w):
        self.l = l
        self.w = w
    
    def area(self):
        return self.l * self.w
    
    def perimeter(self):
        return 2 * (self.l + self.w)

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    
    def area(self):
        return math.pi * self.r**2
    
    def perimeter(self):
        return 2 * math.pi * self.r

# Usage
rect = Rectangle(10, 5)
print("Rectangle Area:", rect.area())
print("Rectangle Perimeter:", rect.perimeter())

circle = Circle(7)
print("Circle Area:", circle.area())
print("Circle Perimeter:", circle.perimeter())

# s = Shape()  ❌ Not allowed (abstract class cannot be instantiated)
