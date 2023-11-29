import sqlite3
import sys


#main
while True:
    print("1.Login\n2.Create account\n3.Logout")
    choice = str(input())
    if choice == "1":
        #Login function
        print("Logged in.")
        #Main Menu
        while True:
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
                print("1.Go Back\n2.View Cart\n3.Add to Cart\n4.Remove from Cart\n5.Check Out")
                choice3 = str(input())
                if choice3 == "1":
                    print("Returning to main menu...")
                elif choice3 == "2":
                    #View Cart
                    print("Viewing cart...")
                elif choice3 == "3":
                    #Add to Cart
                    connection = sqlite3.connect("bookstore.db")
                    cursor = connection.cursor()
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
                    connection = sqlite3.connect("bookstore.db")
                    cursor = connection.cursor()
                    print("What is the ISBN of the book you would like to remove?")
                    book = str(input())
                    cursor.execute("SELECT * FROM inventory AS i, cart AS c WHERE c.UserID = %s AND c.ISBN=\"%s\" AND c.ISBN=i.ISBN" % (USERID HERE, book))
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
                    print("Checking out...")
                else:
                    print("Invalid menu option, returning to main menu...")
            else:
                print("Invalid option. Try again.")
    elif choice == "2":
        #Account Creation
        print("Account created.")
        while True:
            print("")
    elif choice == "3":
        #Logout
        print("Logged out.")
        break
    else:
        print("Invalid option. Try again.")


       
