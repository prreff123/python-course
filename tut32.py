class Employee:
    def __init__(self,aname,asalary,arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetail(self):
        return f"Name is {self.name} ,salary is {self.salary} and role is {self.role}"

harry = Employee("Harry",455,"student")
# rohan = Employee()

# harry.name = "Harry"
# harry.salary = 1200
# harry.role = "Intructor"
# # print(harry.__dict__)

# rohan.name = "Rohan"
# rohan.salary = 455
# rohan.role = "student"
print(harry.salary)