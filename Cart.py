import sqlite3
from Inventory import Inventory

class Cart:
    def __init__(self, databaseName, tableName):
        self.databaseName = databaseName
        self.tableName = tableName
    
    def viewCart(self, userID, inventoryDatabase):
        connection = sqlite3.connect("databasename")
        cursor = connection.cursor()
        cursor.execute("SELECT Title FROM inventory AS i, cart AS c WHERE c.UserID=%s AND c.ISBN=i.ISBN" % (userID))
        cursor.close()
        connection.close()
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
        connection = sqlite3.connect("databaseName")
        cursor = connection.cursor()