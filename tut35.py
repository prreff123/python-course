# multilevel inheritance
class Dad:
    basketball = 1

class Son(Dad):
    dance = 1
    def indance(self):
        return f"Yes I Dance {self.dance} no of times"

class Grandson(Son):
    dance = 6
    def indance(self):
        return f"Jackson yoah!"\
            f" yes I dance very incredible {self.dance} no of times"

darry = Dad()
larry = Son()
harry = Grandson()
print(harry.indance())