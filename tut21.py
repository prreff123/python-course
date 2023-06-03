# l = 10 #Global variable
# def function1 (n):
#     # print(l)
#     l = 5 #Local variable
#     m = 8
#     l = l + 45
#     print(l,m)
#     print(n,"I have printed")

# function1("This is me")
# print(l)    

x = 89
def harry():
    x = 20
    def rohan():
        global x
        x = 80
    # print("before calling rohan",x)
    rohan()
    print("after calling rohan",x) 

harry()
print(x)       