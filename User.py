import sqlite3
import sys

class User:
    con = None
    c = None
    
    def __init__(self, databaseName, tableName):
        self.databaseName = databaseName
        self.tableName = tableName
        self.loggedIn = False
        self.userID = ""
        con = sqlite3(databasename)
        c = con.cursor()
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
        c.execute(cmd)
        con.commit()
        
        
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
        c.execute(cmd, (self.tableName, username, ))
        DatabasePasswords = c.fetchall()
        
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

    def createAccount():

    def getLoggedIn():

    def getUserID():



