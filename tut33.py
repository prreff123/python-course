class Employee:
    def __init__(self,aname,asalary,arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetail(self):
        return f"Name is {self.name} ,salary is {self.salary} and role is {self.role}"

    classmethod
    def change_leave(cls,newleave):
        cls.no_of_leave = newleave    

    # classmethod
    # def from_str(cls,string):
    #     params = string.split("*")
    #     return cls(params[0], params[1], params[2])

harry = Employee("Harry",455,"student")
rohan = Employee("Rohan",255,"contructor")
# karan = Employee.from_str("Karan*265*student")

harry.change_leave(34)
print(harry.no_of_leave)