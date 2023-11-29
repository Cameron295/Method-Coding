import sqlite3
import sys

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
        
        sqCur.execute(UPDATE Inventory SET Stock = Stock - 1 WHERE ISBN)
        
