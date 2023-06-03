# def print2(strl):
#     # print2(strl)
#     print("This is " + strl)

# print2("harry")

# def factorial_recursive(n):

def factorial(n):
    """
    :param n: Integer
    :return: n * n-1 * n-2 * n-3......1 
    #  """ 
    fac = 1
    for i in range(n):
        fac = fac * (i+1)
        return fac
#      n == 1:
#         return 1

#     else:
#         return n *factorial_recursive(n-1)    
    
pass        

number = int(input("Enter the number\n"))
print(factorial(number))
