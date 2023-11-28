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
        connection = sqlite3.connect("databaseName")
        cursor = connection.cursor()
        data = (ISBN, userID, 1)
        cursor.execute("SELECT Quantity FROM cart WHERE UserID=%d AND ISBN=%d" % (userID, ISBN))
        quantity = cursor.fetchall()
        try:
            if (quantity[0][0] > 0):
                cursor.execute("UPDATE cart SET Quantity=%d WHERE UserID=%d AND ISBN=%d" % (quantity[0][0] + 1, userID, ISBN))
        except:
            cursor.execute("INSERT INTO cart (ISBN, UserID, Quantity) VALUES (?,?,?)", data)
        connection.commit()
        cursor.close()
        connection.close()
    def removeFromCart(self, userID, ISBN):
        connection = sqlite3.connect("databaseName")
        cursor = connection.cursor()
        cursor.execute("SELECT Quantity FROM cart WHERE UserID=%d AND ISBN=%d" % (userID, ISBN))
        quantity = cursor.fetchall()
        try:
            if (quantity[0][0] > 1):
                cursor.execute("UPDATE cart SET Quantity=%d WHERE UserID=%d AND ISBN=%d" % (quantity[0][0] - 1, userID, ISBN))
            else:
                cursor.execute("DELETE FROM cart WHERE UserID=%d AND ISBN=%d" % (userID, ISBN))
        except:
            print("Book Does Not Exist")
        connection.commit()
        cursor.close()
        connection.close()
    def checkOut(self, userID):
        connection = sqlite3.connect("databaseName")
        cursor = connection.cursor()