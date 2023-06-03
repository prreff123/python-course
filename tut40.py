# Polymorphism concept
# print(5+6)
# print("5" + "6")
# oops concept is:
"""
Encapsulation
Polymorphism
Abstraction
Inheritance
"""

# overriding concept
class A:
    ClassVar1 = "I am a class vaiable in class A"
    def __init__(self):
        self.var1 = "I am a inside class A's constructor"
        self.ClassVar1 = "Instance var in class A"

class B(A):
    Classvar1 = "I am in class B"
    def __init__(self):
        self.var1 = "I am a inside class B's constructor"
        self.ClassVar1 = "Instance var in class B"


a = A()
b = B()
print(b.ClassVar1)            