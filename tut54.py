a = input("What is your name ")
if a.isnumeric():
    raise Exception("Numbers are not allowed")
print(f"Hello {a} ")    

# == - value equality - Two objects have the same value
# is - reference equality two references refer to the same object