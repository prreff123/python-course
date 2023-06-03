# try:
#     f = open("does.txt") 
# except Exception as e:
#     print(e)    

# print("Important stuff")

def searcher():
    import time
    book = "This is a book on harry and code with harry and good"
    time.sleep(4)

    while True:
        text = (yield)
        if text in book:
            print("Your text is in the book")
        else:
            print("Text is not in the book")
search = searcher()
next(search)
search.send("Harry")
input("press any key")
search.send("PJ Jain")               