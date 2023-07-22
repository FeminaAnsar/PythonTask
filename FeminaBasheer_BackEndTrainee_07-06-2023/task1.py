#1) Create a class named Shape. Add an instance method called area. But don't define the method, just raise NotImplemented()
# exception with a message
class Shape:
    def area(self):
        raise NotImplementedError("Not Implemented Error")
obj1=Shape()
obj1.area()
