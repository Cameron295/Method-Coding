import sqlite3
import sys



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
