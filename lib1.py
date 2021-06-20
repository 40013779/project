'''import sys'''
import sys
class Library:
    '''library'''
    def __init__(self, list, name):
        self.bookslist = list
        self.name = name
        self.lenddict = {}
    def displaybooks(self):
        '''display books'''
        print('the books are :')
        for book in self.bookslist:
            print(book)
    def lendbook(self, user, book):
        '''book lending'''
        if book not in self.lenddict.keys():
            self.lenddict.update({book:user})
            print("Lender-Book database has been updated. You can take the book now")
        else:
            print(f"Book is already being used by {self.lenddict[book]}")
    def addbook(self, book):
        '''adding book'''
        self.bookslist.append(book)
        print("Book has been added to the book list")
    def returnbook(self,book):
        '''book return'''
        if book in self.lenddict.keys():
            print('book was returned')
            self.lenddict.pop(book)
        else:
            print('book was not lended')
object = Library(['Python', 'java','c','c++'], "Code")
while(True):

    print(f"Welcome to the {object.name} library. Enter your choice to continue")
    print("1. Display Books")
    print("2. Lend a Book")
    print("3. Add a Book")
    print("4. Return a Book")
    USER_CHOICE = input('enter :')
    if USER_CHOICE not in ['1','2','3','4']:
        print("Please enter a valid option")
    else:
        USER_CHOICE= int(USER_CHOICE)
    if USER_CHOICE == 1:
        object.displaybooks()
    elif USER_CHOICE == 2:
        book = input("Enter the name of the book you want to lend:")
        user = input("Enter your name :")
        object.lendbook(user, book)
    elif USER_CHOICE == 3:
        book = input("Enter the name of the book you want to add:")
        object.addbook(book)
    elif USER_CHOICE == 4:
        book = input("Enter the name of the book you want to return:")
        object.returnbook(book)
    else:
        print("Not a valid option")
    print("Press q to quit and c to continue")
    USER_CHOICE2 = ""
    while(USER_CHOICE2!="c" and USER_CHOICE2!="q"):
        USER_CHOICE2 = input()
        if USER_CHOICE2 == "q":
            sys.exit()
        elif USER_CHOICE2 == "c":
            continue
