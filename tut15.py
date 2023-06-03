# num1 = int(input())
# num2 = int(input())
# print("Enter the number of num1\n Enter the number of num2" , num1*num2)

print("Enter the num1")
num1 = input()
print("Enter the num2")
num2 = input()

# Error Exception Handling
try:
    print("The multiply of these two numbers is", int(num1)*int(num2))

except Exception as e:
    print(e)    

print("This line is very important")    