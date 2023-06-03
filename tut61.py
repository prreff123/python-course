def next_pallindrome(n):
    n = n+1
    while not is_pallindrome(n):
       n += 1
    return n
    
def is_pallindrome(n):
    return str(n) == str(n)[::-1]

if __name__ == "__main__":

    n = int(input("Enter the number of test cases\n"))
    numbers = []

    for i in range(n):
        number = int(input("enter the number\n"))
        numbers.append(number)

      # print(numbers)
    for i in range(n):
      print(f"Next pallindrome for {numbers[i]} is {next_pallindrome(numbers[i])}")