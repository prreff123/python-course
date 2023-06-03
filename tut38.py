# protected member
class Student:
    _name = None
    _roll = None
    _branch = None

    def __init__(self,name,roll,branch):
        self._name = name
        self._roll = roll
        self._branch = branch

    def _displayRollandBranch(self):
        print("Roll: ", self._roll)
        print("Branch: ", self._branch)

class geek(Student):
    def __init__(self, name, roll, branch):
        Student.__init__(self,name,roll,branch)

    def DispalyDetails(self):
        print("Name: ", self._name)
        self._displayRollandBranch()

obj = geek("R2h",141,"Information Technology")
obj.DispalyDetails()