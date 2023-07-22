#2) Make it an abstract base class by inheriting ABC class from the abc module. (To import: from abc import ABC)
#Make the area method an abstract method by decorating it with abstractmethod decorator (import this also from abc).

from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        raise NotImplementedError("Not Implemented Error")
class NewShape(Shape):
    def area(self):
        raise NotImplementedError("Not Implemented Error")

obj1=NewShape()
obj1.area()