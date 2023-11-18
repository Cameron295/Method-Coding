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
         INSERT INTO %s VALUES(%s, $s,%s,%s,%s,%s,%s,%s,%s);

         """

    def getLoggedIn():

        return self.loggedIn

    def getUserID():

        return self.userID

