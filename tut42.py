# Abstraction 
from abc import ABCMeta, abstractclassmethod

class shape(metaclass = ABCMeta):
    @abstractclassmethod
    def printarea(self):
        return 0

class Rectangle(shape):
    type = "Rectangle"
    sides = 4

    def __init__(self):
        self.length = 6
        self.breadth = 7

    def printarea(self):
        return self.length * self.breadth

rect1 = Rectangle()
print(rect1.printarea())