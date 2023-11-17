import sqlite3
import sys


#cart
class Cart:
    def __init__(self, databaseName, tableName):
        self.databaseName = databaseName
        self.tableName = tableName
    
    def viewCart(self, userID, inventoryDatabase):
        
    def addToCart(self, userID, ISBN):
        #doesn't handle quantity yet
        connection = sqlite3.connect("databaseName")
        cursor = connection.cursor()
        data = (ISBN, userID, 1)
        cursor.execute("INSERT INTO cart (ISBN ,UserID, Quantity) VALUES (?,?,?)", data)
        connection.commit()
        cursor.close()
        connection.close()
    def removeFromCart(self, userID, ISBN):
        #doesn't handle quantity yet
        connection = sqlite3.connect("databaseName")
        cursor = connection.cursor()
        data = (userID, ISBN)
        cursor.execute("DELETE FROM cart WHERE UserID=? AND ISBN=?", data)
        connection.commit()
        cursor.close()
        connection.close()
    def checkOut(self, userID):
        
    


#inventory





#user

class User:

    def __init__(self, databaseName, tableName, loggedIn, userID):
        self.databaseName = databaseName
        self.tableName = tableName
        self.loggedIn = loggedIn
        self.userID = userID

    def login():

    def logout():

    def viewAccountInformation():

    def createAccount():

    def getLoggedIn():

    def getUserID():








#main






