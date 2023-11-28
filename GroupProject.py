import sqlite3
import sys


#main

menu = True
while menu
       print("""" 1. Login 
                  2. Create Account 
                  3. Logout
                  4.Exit """")
             
       ans= input("please select a number: ")
                  if ans=="1":


                elif ans=="2":


                elif ans=="3":


                elif ans=="4":
                break

                else :
                print ("/n Not a Valid Choice Try agin")






CREATE TABLE   User 
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

CREATE TABLE   Inventory 
        ( ISBN varchar(255),
        Title varchar(255), 
        Author varchar(255),
        Genre varchar(255),
        Pages varchar(255),
        ReleaseDate varchar(255),
        Stock int,
        PRIMARY KEY (ISBN) );
       
