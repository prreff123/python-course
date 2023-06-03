# Single inheritance concept

class person(object):

    # constructor
    def __init__(self,name):
        self.name = name

    def getName(self):
        return self.name

    def isEmployee(self):
        return False

class Employee(person):
    def isEmployee(self):
        return True

emp = person("Geek1")
print(emp.getName(),emp.isEmployee())

emp = Employee("Geek2")
print(emp.getName(),emp.isEmployee())

