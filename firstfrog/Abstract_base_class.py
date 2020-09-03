from abc import ABC ,abstractmethod
class Shape(ABC):
    @abstractmethod
    def printdetails(self):
        return 0

class Rectangle(Shape):
    def __init__(self):
        self.length=6
        self.width=7

    def printdetails(self):
        return f'area of rectangle ',self.length * self.width
rect=Rectangle()
print(rect.printdetails())
# print(rect.printdetails())
class Square(Shape):
    def __init__(self):
        self.side=4
        self.one_side=7
    def printdetails(self):
        return f'area of rectangle ',self.side * self.one_side
sqr=Square()
print(sqr.printdetails())

