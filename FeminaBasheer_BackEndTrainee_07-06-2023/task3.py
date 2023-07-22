#3) Add 4 different subclasses for class Shape. - Triangle, Square, Pentagon, Circle.
# Define custructor for each of them to assign the necessary parameters required for calculating the area.
# Define the area method for each of the classes. When invoked it Should return the area of the shape by calculating it.
# Create an object for each of the subclasses and call the area method on the objects.

from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Triangle(Shape):
    def __init__(self,b,h):
        self.b=b
        self.h=h
    def area(self):
        print("Area of Triangle:",(self.b*self.h)/2)

class Square(Shape):
    def __init__(self,s):
        self.s = s

    def area(self):
        print("Area of Square:", (self.s * self.s))

class Pentagon(Shape):
    def __init__(self,a,b):
        self.a= a
        self.b = b

    def area(self):
        print("Area of Pentagon:", ((5*self.a * self.a) / 2))

class Circle(Shape):
    def __init__(self,r):
        self.r = r

    def area(self):
        print("Area of Circle:", (3.14*self.r*self.r))

t=Triangle(10,20)
t.area()
sq=Square(20)
sq.area()
p=Pentagon(30,20)
p.area()
c=Circle(25)
c.area()