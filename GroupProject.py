import sqlite3
import sys

#INVENTORY CLASS
class Inventory:
    def __init__(self, databaseName, tableName):
        self.databaseName = databaseName
        self.tableName = tableName

    # displays all items currently in the inventory
    def viewInventory():
        # connection and cursor variables
        sqConn = sqlite3.connect('databaseName.db')
        sqCur = sqConn.cursor()
    
        sqCur.execute(SELECT * FROM Inventory)
        print(sqCur.fetchall())
    
    # asks for a title from the user, then checks for any matches in the database and returns the result
    # if it's a successful search, displays all results to user. If unsuccessful, informs the user their search failed.
    def searchInventory():
        # connection and cursor variables
        sqConn = sqlite3.connect('databaseName.db')
        sqCur = sqConn.cursor()
        
        # taking search input from user
        search_title = input("Search Title: ")

        search_return = sqCur.execute(SELECT * FROM Inventory WHERE Title LIKE "%" + search_title + "%")
        
        # successful search
        if search_return != None:
            print(sqCur.fetchall())

        # unsuccessful search
        else:
            print("Your search failed to return any results. Check your spelling or try again with a different title.")
        
    # decreases stock number of the given ISBN's respective item
    def decreaseStock(ISBN):
        # connection and cursor variables
        sqConn = sqlite3.connect('databaseName.db')
        sqCur = sqConn.cursor()

        # updating stock
        sqCur.execute(UPDATE Inventory SET Stock = Stock - 1 WHERE ISBN=%s)


#USER CLASS
class User:
    connection = None
    cursor = None
   
    def __init__(self, databaseName, tableName):
        self.databaseName = databaseName
        self.tableName = tableName
        self.loggedIn = False
        self.userID = ""
        connection = sqlite3("databasename")
        cursor = connection.cursor()
        cmd= "CREATE TABLE IF NOT EXISTS "+ tableName + """ 
        ( UserID varchar(255),
        Email varchar(255), 
        Password varchar(255),
        FirstName varchar(255),
        LastName varchar(255),
        Address varchar(255),
        City varchar(255),
        State varchar(255),
        Zip varchar(255), 
        Payment varchar(255), 
        PRIMARY KEY (UserID) );
        """
        cursor.execute(cmd)
        connection.commit()
        
        
    def __init__(self):
        self.databaseName = ""
        self.tableName = ""
        self.loggedIn = False
        self.userID = ""
        
    def login():
        #get username and password from user
        username= input("UserID: ")
        password= input("Password: ") 

        cmd = """
        SELECT Password FROM %s 
        WHERE UserID = %s ;

        """
         cursor.execute(cmd, (self.tableName, username, ))
        DatabasePasswords = cursor.fetchall()
        
        if len(DatabasePassword)!=0 and password == DatabasePasswords[0]: 
            self.userID = username
            self.loggedIn = True
            return True

        else: 
            return False
    def logout():

        self.userID = ""
        self.loggedIn = False
        return False

    def viewAccountInformation():
        # view all in table with useID in SQL
         Username= input("UserID: ")

        cmd = """ 
         Create View %s AS 
         SELECT  UserID,Email, Password, FirstName, Lastname, Address, City, State, Zip, Payment
         From %s 
         Where UserID ="%s";
         """
        cursor.execute(cmd, (self.tableName,????, Username))
    def createAccount():
        #will insert new info into table SQL

        UserID = input ("UserID: ")
        Email input ("Email: ") 
        Password input ("Password: ")
        FirstName input ("First Name: ")
        LastName input ("Last Name: ")
        Address input ("Address: ")
        City input ("City: ")
        State input ("State: ")
        Zip input ("Zip: ") 
        Payment input ("Payment: ") 

         cmd = """ 
         INSERT INTO %s VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);

         """
        cursor.execute(cmd, (self.tableName, UserID,Email, Password, FirstName, Lastname, Address, City, State, Zip, Payment))

    def getLoggedIn():

        return self.loggedIn

    def getUserID():

        return self.userID


#CART CLASS
class Cart:
    def __init__(self, databaseName, tableName):
        self.databaseName = databaseName
        self.tableName = tableName

    def viewCart(self, userID, inventoryDatabase):
        connection = sqlite3.connect(self.databaseName)
        cursor = connection.cursor()
        cursor.execute("SELECT Title FROM %s AS i, %s AS c WHERE c.UserID=%s AND c.ISBN=i.ISBN" % (inventoryDatabase, self.tableName, userID))
        result = cursor.fetchall()
        if result == []:
            print("Your cart is empty.")
        else:
            print("Books in your cart:")
            for x in result:
                for y in x:
                    print(y)
        cursor.close()
        connection.close()

    def addToCart(self, userID, ISBN):
        connection = sqlite3.connect(self.databaseName)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM %s WHERE UserID=%s AND ISBN=\"%s\"" % (self.tableName, userID, ISBN))
        quantity = cursor.fetchall()
        try:
            if (quantity[0][2] > 0):
                cursor.execute("UPDATE %s SET Quantity=%d WHERE UserID=%s AND ISBN=\"%s\"" % (self.tableName, quantity[0][2] + 1, userID, ISBN))
        except:
            cursor.execute("INSERT INTO %s (ISBN, UserID, Quantity) VALUES (\"%s\",%s,%d)" % (self.tableName, ISBN, userID, 1))
        connection.commit()
        cursor.close()
        connection.close()

    def removeFromCart(self, userID, ISBN):
        connection = sqlite3.connect(self.databaseName)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM %s WHERE UserID=%s AND ISBN=\"%s\"" % (self.tableName, userID, ISBN))
        quantity = cursor.fetchall()
        try:
            if (quantity[0][2] > 1):
                cursor.execute("UPDATE %s SET Quantity=%d WHERE UserID=%s AND ISBN=\"%s\"" % (self.tableName, quantity[0][2] - 1, userID, ISBN))
            else:
                cursor.execute("DELETE FROM %s WHERE UserID=%s AND ISBN=\"%s\"" % (self.tableName, userID, ISBN))
        except:
            print("That book is not in your cart.")
        connection.commit()
        cursor.close()
        connection.close()

    def checkOut(self, userID):
        connection = sqlite3.connect(self.databaseName)
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM %s WHERE UserID=%s" % (self.tableName, userID))
        result = cursor.fetchall()
        if result == []:
            print("Your cart is empty.")
        else:
            print("Checking out...")
            for x in result:
                for y in range(x[2]):
                    #decrease stock not yet added from inventory class
                    cursor.execute("SELECT Quantity FROM cart WHERE UserID=%s AND ISBN=\"%s\"" % (x[1], x[0]))
                    quantity = cursor.fetchall()
                    try:
                        if (quantity[0][0] > 1):
                            cursor.execute("UPDATE %s SET Quantity=%d WHERE UserID=%s AND ISBN=\"%s\"" % (self.tableName, quantity[0][0] - 1, x[1], x[0]))
                        else:
                            cursor.execute("DELETE FROM %s WHERE UserID=%s AND ISBN=\"%s\"" % (self.tableName, x[1], x[0]))
                    except:
                        print("Book removal failed.")
                    connection.commit()
        cursor.close()
        connection.close()


#main
cart = Cart("group8.db", "Cart")
while True:
    # menu options for logging in, creating an account, and logging out
    print("1.Login\n2.Create account\n3.Logout")
    # user input
    choice = str(input())
    if choice == "1":
        #Login function
        print("Logged in.")
        #Main Menu
        while True:
            # menu options for logging out, looking at account information, viewing inventory information, and accessing the cart
            print("1.Logout\n2.Account\n3.Inventory\n4.Cart")
            choice2 = str(input())
            if choice2 == "1":
                #Logout
                print("Logging out...")
                break
            elif choice2 == "2":
                #View Account Information
                print("Account Info")
            elif choice2 == "3":
                # menu options for returning to the last page, viewing inventory, and searching inventory
                print("1.Go Back\n2.View Inventory\n3.Search Inventory")
                choice3 = str(input())
                if choice3 == "1":
                    print("Returning to main menu...")
                elif choice3 == "2":
                    #View Inventory
                    print("Viewing inventory...")
                elif choice3 == "3":
                    #Search Inventory
                    print("Searching inventory...")
                else:
                    print("Invalid menu option, returning to main menu...")
            elif choice2 == "4":
                # menu options for returning to the last page, viewing cart, adding/removing an item from the cart, and checking out
                print("1.Go Back\n2.View Cart\n3.Add to Cart\n4.Remove from Cart\n5.Check Out")
                choice3 = str(input())
                if choice3 == "1":
                    print("Returning to main menu...")
                elif choice3 == "2":
                    #View Cart
                    cart.viewCart(USERID HERE, "Inventory")
                elif choice3 == "3":
                    #Add to Cart
                    connection = sqlite3.connect("group8.db")
                    cursor = connection.cursor()
                    # taking input selection from user for ISBN, recorded into variable "book"
                    print("What is the ISBN of the book you would like to add?")
                    book = str(input())
                    cursor.execute("SELECT TITLE, ISBN FROM Inventory WHERE ISBN=\"%s\"" % (book))
                    x = cursor.fetchall()
                    try:
                         cart.addToCart("USERID GOES HERE", x[0][1])
                         print("%s was added to your cart." % (x[0][0]))
                    except:
                         print("That book does not exist.")
                    cursor.close()
                    connection.close()
                elif choice3 == "4":
                    #Remove from Cart
                    connection = sqlite3.connect("group8.db")
                    cursor = connection.cursor()
                    # taking input selection from the user for ISBN, recorded into variable "book"
                    print("What is the ISBN of the book you would like to remove?")
                    book = str(input())
                    cursor.execute("SELECT * FROM inventory AS i, cart AS c WHERE c.UserID = %s AND c.ISBN=\"%s\" AND c.ISBN=i.ISBN" % (USERID here, book))
                    x = cursor.fetchall()
                    try:
                         cart.removeFromCart(USERID HERE, x[0][0])
                         print("%s was removed from your cart." % (x[0][1]))
                    except:
                         print("That book is not in your cart.")
                    cursor.close()
                    connection.close()
                elif choice3 == "5":
                    #Checkout
                    cart.checkOut(USERID HERE)
                else:
                    print("Invalid menu option, returning to main menu...")
            else:
                print("Invalid option. Try again.")
    elif choice == "2":
        #Account Creation
        print("Account created.")
    elif choice == "3":
        #Logout
        print("Logged out.")
        break
    else:
        print("Invalid option. Try again.")


       
