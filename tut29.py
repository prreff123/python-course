# numbers = ["3","34","64"]
# numbers = list(map(int,numbers))

# # for i in range(len(numbers)):
# #     numbers[i] = int(numbers[i])

# numbers[1] = numbers[1] + 1
# print(numbers[1])

# def sq(a):
#     return a*a

# num = [2,3,4,5,2,54,59,8]
# square = list(map(lambda x: x*x,num))
# print(square)       

from functools import reduce

list1 = [1,2,3,4]
num = reduce(lambda x,y:x+y, list1)
print(num)