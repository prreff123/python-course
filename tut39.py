# private member
class Geek:
    __name = None
    __roll = None
    __branch = None

    def __init__(self,name,roll,branch):
        self.__name = name
        self.__roll = roll
        self.__branch = branch

    def __DispalyDetails(self):
        print("Name: ", self.__name)
        print("roll: ", self.__roll)
        print("branch: ", self.__branch)

    def AccessPrivateFinction(self):
        self.__DispalyDetails()

obj = Geek("R2h",145,"Information Technology")
obj.AccessPrivateFinction()