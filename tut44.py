"""
iterable - __iter__() or __getitem__()
Iterator - __next__()
Iteration - 
"""

def gen(n):
    for i in range(n):
        yield i

# g = gen(26652454850)
# print(g)        
g = gen(3)
for i in g:
    print(i)