'''
main.py
Library Managment System
Date Created: 11-8-19
Author: Madie Struwe

This project will be a Library Managment System
Will be able to
-Add Books
-Remove Books
-Add Members
-Allocate Books to Members
-Deallocate Books to Members

This file contains the main menu for the project
other files will be called to perform specifed
functions
'''
#import helper libaries
import os
#import helper files
import book_list as bl

'''
this is the main function
It contains the main menu
'''

def main():
    #this is to get the absolute path to the Inventory.txt
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER, "Inventory.txt")
    #Display the one time welcome message
    print("Welcome to the Library Managment System\n\
           Author: Madie Struwe")
    #go back to the menu after an operation
    #until the user desides to quit
    while (True):
        #show the options
        print("1. Display Books")
        try:
            choice=int(input("Pick something: "))
            if(choice==1):
                #open the inventory
                with open(my_file,"r") as books:
                    lines=books.read()
                    print(lines)
                    print()
        #if unexpected input, throw an error
        except ValueError:
            print("Please input a numeric value")
        #bl.book_list
        #print("ran book_list")

#run the main function
main()