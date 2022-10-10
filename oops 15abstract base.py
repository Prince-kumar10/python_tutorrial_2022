# abstract base in python

from abc import ABC  ,abstractmethod
class shape(ABC):
     @abstractmethod
     def printrea(self):
         return 0


class Rectangle(shape):
    type = "rectangle"
    sides = 4
    def __init__(self):
        self.langth  = 2
        self.breadth = 3

    def printrea(self):
        return self.langth * self.breadth

abstr1 = Rectangle()
print(abstr1.printrea())

