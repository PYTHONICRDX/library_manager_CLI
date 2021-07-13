""" I have made the previous library system based on an Idea of basic library uses
In this one I am gonna make some enhancements mainly incluidibg the following.

Beta features :
These features have been introduiced as a modification to the previous version
1. Book code : To acess books in an index specific way.
2. Genre : Species what the books' content deals with. Can be easily searched up by the user.
3. Menu driven and easy to use.
4. Enhanced fine calculation scheme.
5. Data storage modifications.
6. Making books standard specific.Indicating age indirectly(ex : for and above class 6).
7. User has to pay the price of the book if lost.
8. Voice feature removed due to delay caused by it's execution time.
9. Program is dynamic as data is not erased as the program.
      Code comments added to make it readable by others


REQUIREMENTS FOR RUNNING THE PROGRAM : 
      1. MongoDB(Either server or local db. Both works)
      2. MongoShell(preffered for programmers) / MongoDB Compass to view, edit, update databases
      3. python interpreter(visit :  www.python.org)
      4. Pymongo extension to connect MongoDB to python
------------------------------------------------------------------------------------------THAT'S ALL------------------------------------------------------------------------------
"""

import pymongo #Module that acts as a driver to connect me to a database in my pymongo localhost

from datetime import date

client = pymongo.MongoClient("mongodb://127.0.0.1:27017") # client to establish connection with the database
db = client.books4 #There is a database in my mongo db localhost named books4. db variable acesses the path to that database

books = db.bklist #There is a collection in my books4 database named bklist. It stores the documents(fields and values for all lists)

#This function is used to buy stock
def stockpile():
    name = input("Enter name of the book : ") #Takes in the name of the book as an input from the user
    author = input("Enter name of the book's author : ") #Takes in the author's name of the book as an input from the user
    genre = input("Enter what genre the book belongs to : ").lower() #Takes in the genre of the book as an input from the user
    code = input("Specify a permanant code for the book : ") #Takes in the unique code(ISBN in real life scenario) of the book as an input from the user
    standard = input("Enter standard to specify for children of which standard this book is meant for : ") #Takes in the standard of student above which the book should be read(Since this library has been designed to be a school library.
    cost = input("Enter the cost of the book : ") #Takes in the price of the book as an input from the user
#Takes all the book info required
    doc = {"bookname":name,"author":author,"genre":genre,"standard":standard,"code":code,"cost" : cost,"availability":"available"} #Transforms all the data into library format(json/bson : object)
    books.insert_one(doc)#Inserts the document into the collection
#complementary function for buying stock
def stockpiler():#To specify the number of times the above function is to be called (Directly proportional to the number of books)
      n = int(input("Enter the number of entries to be made : "))
      for i in range(n):
            stockpile()
            print("Received data for this book. \n")

#To view all books
def showall():
    n = 1#Initial counter
    for book in books.find():
        obj = {}#dictionaries(json objects) to store certain keys & values(fields & values)
        obj2 ={}
        obj["book name"] = book["bookname"]#implementation of the above dictionary(object)
        obj2["auth"] = book["author"]
        print(n , obj["book name"] , " by ",obj2["auth"])#Printing the book name along with the name of it's Author
        n= n + 1#Counter increment

# This function will allow the user to view details and borrow the book
def search_by_name_and_borrow(): #To query a book by it's name in order to borrow/not borrow a book.
    n = input("Enter the name of the book that you want : ")#Takes the bookname as an input
    n = n.title()
    print("\n\n")
    for book in books.find({"bookname" : n}):#Same query technique as showall but here the parameter values have been specified
        a = {}#Similar dictionaries(objects) as used in showall() 
        b = {}
        c = {}
        d = {}
        e = {}
        print("Your book is : ",n) #Displaying all the information of the book in specific
        a["author name"] = book["author"]
        print("The author of this book is",a["author name"],".")
        b["gen"] = book["genre"]
        print("Genre",b["gen"])
        c["Code"] = book["code"]
        print("Unique book ID is : ",c["Code"])
        d["Std"] = book["standard"]
        print("Recommended for children for and above standard",d["Std"])
        e["av"] = book["availability"]
        print("Currently ",e["av"])
    print("Would you like to borrow this book ?")
    inp = input(("Enter yes or no : ")).lower()#Asking whether the book is to be borrowed or not
    print("\n")
    if inp == "yes":# Execution upon yes
        books.update_one({"bookname":n},{"$set":{"availability":"unavailable"}},upsert=False)
        print("Thank You for borrowing the book. Please make sure that you return it within 10 days.")
    elif inp == "no":#Else nullifies
        pass

#To search a book genre specifically
def search_by_genre():
    n = input("Enter the genre of the book(s) you want to get : ")
    n = n.lower()
    i = 0
    for book in books.find({"genre":n}): #Similar query as used in all other cases(refer showall function comments for more details.)
        obj = {}
        obj2 = {}
        obj3 ={}
        obj["Book name"] = book["bookname"]
        obj2["av"] = book["availability"]
        obj3["auth"] = book["author"]
        i = i + 1
        print(i ,". ", obj["Book name"] ,"  by",obj3["auth"], ". Currently ",obj2["av"])
    if i == 0:
        print("Looks like there are not too many great matches for your choice. Maybe you should try checking the spelling.")

#To search the book author specifically
def search_by_author():
    n = input("Enter the author of the book(s) you want to get : ")
    n = n.title()
    i = 0
    for book in books.find({"author":n}):
        obj = {}
        obj2 = {}
        obj3 ={}
        obj["Book name"] = book["bookname"]
        obj2["av"] = book["availability"]
        obj3["auth"] = book["author"]
        i = i + 1
        print(i ,". ", obj["Book name"] ,"  by",obj3["auth"], ". Currently ",obj2["av"])
    if i == 0:
        print("Looks like there are not too many great matches for your choice. Maybe you should try checking the spelling.")
    else:
        pass

#Searching by book code
def search_by_bkcode():
    n = input("Enter the book code of the book you want to get. You can enter code in any case but make sure that the code is exact : ")
    n = n.upper()
    i = 0
    for book in books.find({"code":n}):
        obj = {}
        obj2 = {}
        obj3 ={}
        obj["Book name"] = book["bookname"]
        obj2["av"] = book["availability"]
        obj3["auth"] = book["author"]
        i = i + 1
        print(i ,". ", obj["Book name"] ,"  by",obj3["auth"], ". Currently ",obj2["av"])
    if i == 0:
        print("Looks like there are not too many great matches for your choice. Maybe you should try checking the spelling.")

#Viewing all available books
def search_by_availability():
    i = 0
    print("Currently available books are as follows : \n")
    for book in books.find({"availability":"available"}):
        obj = {}
        obj2 = {}
        obj3 ={}
        obj["Book name"] = book["bookname"]
        obj3["auth"] = book["author"]
        i = i + 1
        print(i ,". ", obj["Book name"] ,"  by",obj3["auth"], ".")
    if i == 0:
        print("Looks like there are not too many great matches for your choice. Maybe you should try checking the spelling.")    

#To return a book
def book_return():
    n = input("Enter the name of the book that you want to return : ")
    n = n.title()
    books.update_one({"bookname":n},{"$set":{"availability":"available"}},upsert=False)
    fine_calculation()
    print("Thank you for returning the book")

#To be used in case book has been lost by student
def lost():
    inp = input("Enter the name of the book that you have lost : ")
    inp = inp.title()
    n = 0
    inp2 = input("Enter your name standard and section seperated by spaces")
    for book in books.find({"bookname":inp}):
        obj = {}
        obj["bcost"] = book["cost"]
        n = n + 1
    if n > 0:
        strx = "lost by "+inp2
        print("Compensation to be paid of INR : ",obj["bcost"],".")
        books.update_one({"bookname":inp},{"$set":{"attribute":strx}},upsert=True)
    else:
        print("Please recheck the spelling of your book.")
    print("Is the transaction complete?")
    n = input("Enter yes or no : ")
    del_doc = {"bookname":inp}
    if n == "yes":
        books.delete_one(del_doc)
    else:
        pass

#Calculates fine in case of late return
def fine_calculation():#Late charges calculated here by subtracting the day when the book has been borrowed from the current date. If-else logic used to execute the cause.
    current_date = date.today() 
    y =  current_date.year
    m =  current_date.month
    d = current_date.day
    f_date = date(int(input("enter year when the book was borrowed: ")), int(input("enter month when the book was borrowed : ")), int(input("enter date when the book was borrowed : ")))
    l_date = date(y, m, d)
    delta = l_date - f_date
    late =delta.days
    late = late - 10
    if late > 0:
        fine = late * 2
        print("Due to a late return a fine of rupees ",fine," has been generated.")
    else:
        print("Book has been returned within time. No fine generated.")

#logic
if __name__ == "__main__":
    print("Welcome to virtual library of Lions Vidya Mandir")# This is to be printed in the beginning to Welcome anyone in case he/she visits the library.
    cmd = " Enter 1 to see all books \n Enter 2 to see available books \n Enter 3 to search a book by it's name\n Enter 4 to search book by author name \n Enter 5 to search book by genre \n Enter 6 to search book by code \n Enter 7 to return a book\n Enter 8 to buy stocks or receive donation \n Enter 9 if you have lost your book \n Enter 0 to exit"
    while True:#Infinite loop that makes the system work as long as explicit termination command is no given by the user.
        print(cmd) #Default Commands to be printed every time after the execution of each function for user assistance.
        n =int(input("Enter your choice : "))
        print("\n")
        if n == 1:#The user needs to drive the menu according to the numbers specified for each task(0 - 9). According to the input of the user, the simple if else ladder is executed
            showall()
            print("\n")
        elif n == 2:
            search_by_availability()
            print("\n")
        elif n == 3:
            search_by_name_and_borrow()
            print("\n")
        elif n == 4:
            search_by_author()
            print("\n")
        elif n == 5:
            search_by_genre()
            print("\n")
        elif n == 6:
            search_by_bkcode()
            print("\n")
        elif n == 7:
            book_return()
            print("\n")
        elif n == 8:
            stockpiler()
            print("\n")
        elif n == 9:
            lost()
            print("\n")
        elif n == 0:
            print("Thank You for visiting the school library.")
            print("\n")
            exit() #Termination command to be activated in case the input given by the user is 0.
