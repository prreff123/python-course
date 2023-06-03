# program to access public modifier
# public()
# protected(_)
# private(__)
class Geek:
    def __init__(self,name,age):
        self.geekname = name
        self.geekage = age

    def displayAge(self):
        print("Age: ", self.geekage)

obj = Geek("R2j",21)
print("Name: ", obj.geekname)
obj.displayAge()          
