import sqlite3
import sys

class User:
    connection = None
    cursor = None
   
    def __init__(self, databaseName, tableName):
        self.databaseName = databaseName
        self.tableName = tableName
        self.loggedIn = False
        self.userID = ""
        connection = sqlite3.connect("databasename")
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
        connection = sqlite3.connect("databasename")
        cursor = connection.cursor()
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
        connection = sqlite3.connect("databasename")
        cursor = connection.cursor()
        # view all in table with useID in SQL
         Username= input("UserID: ")

        cmd = """ 
         Create View %s AS 
         SELECT  UserID,Email, Password, FirstName, Lastname, Address, City, State, Zip, Payment
         From %s 
         Where UserID ="%s";
         """
        cursor.execute(cmd, (self.tableName,User, Username))
    def createAccount():
        connection = sqlite3.connect("databasename")
        cursor = connection.cursor()
        #will insert new info into table SQL

        userID = input ("UserID: ")
        email = input ("Email: ") 
        password = input ("Password: ")
        firstName = input ("First Name: ")
        lastName = input ("Last Name: ")
        address = input ("Address: ")
        city = input ("City: ")
        state = input ("State: ")
        zip = input ("Zip: ") 
        payment = input ("Payment: ") 
        
         cmd = """ 
         INSERT INTO %s VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);

         """
        cursor.execute(cmd, (self.tableName, userID,email, password, firstName, lastname, address, city, state, zip, payment))

    def getLoggedIn():

        return self.loggedIn

    def getUserID():

        return self.userID

