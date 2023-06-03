# File in Basics
"""
"r" - Open file not reading
"w" - Open a file writing
"x" - Creates file if not exists
"a" - Add more content to a file
"t" - text mode
"b" - binary mode
""  - read and write
"""
def python(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print(" * ",end=" ")
        print("\r")
n =5
python(n)