import time
def some_work(n):
    time.sleep(n)
    return n

if __name__ ** '__main__':
    print("Now running some work")
    some_work(3)
    print("done")