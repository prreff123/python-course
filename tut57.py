class Library:
    def __init__(self, list,name):
        self.booklist = list
        self.name = name
        self.lendict = {}

    def displaybooks(self):
        print(f"we have following books in our library:{self.name}")
        for book in self.booklist:
            print(book)

    def lendbook(self,user,book):
        if book not in self.lendict.keys():
            self.lendict.update({book:user})
            print("lender-book database has been updated.you can take the book now")

        else:
            print(f"Book is already being used by {self.lendict[book]}")    

    def addbook(self,book):
        self.booklist.append(book)
        print("book has been added to the book list")    

    def returnbook(self,book):
        self.lendict.pop(book)

if __name__ == "main":
    harry = Library(['python','Rich daddy poor daddy','harry potter','c basics','algorithms by CLRs'],"codewthharry")

    while(True):
        print(f"Welcome to the {harry.name} Library. Enter your choice to continue")
        print("1. Display Book")
        print("2. Lend a book")
        print("3. Add a book")
        print("4. Return a book")

        user_choice = input()
        if user_choice not in ['1','2','3','4']:
            print("please enter a valid opton")
            continue
        else:
            user_choice = int(user_choice)

        if user_choice == 1:
            harry.displaybooks()

        elif user_choice == 2:
            book = input("Enter the name of the book you want to lend")
            user = input("Enter your name")
            harry.lendbook(user,book)

        elif user_choice == 3:
            book = input("Enter the name of the book you want to add")
            harry.addbook(book)

        elif user_choice == 4:
            book = input("Enter the name of book you want to return")
            harry.returnbook(book)

        else:
            print("Not a valid option")

        print("press q to quit and c to continue")
        
        user_choice2 = ""
        while(user_choice2!="c" and user_choice2!="q"):
            user_choice2 = input()
            if user_choice2 == "q":
                exit()
            if user_choice2 == "c":
                continue     