import random
def rohanmultiplication(number):
    wrong = random.randint(0,9)
    table = [i * number for i in range(1,11)]
    table[wrong] = table[wrong] * random.randint(0,10)
    return table

def iscorrect(table,number):
    for i in range(1,11):
        if table[i-1] !=  i*number:
            return i-1


if __name__ == "__main__":
    # print(rohanmultiplication(7))
    number = int(input("Enter a number: "))
    mytable = rohanmultiplication(number)
    print(mytable)
    wrongindex = iscorrect(mytable,number)
    print(f"the table is wrong index {wrongindex}")