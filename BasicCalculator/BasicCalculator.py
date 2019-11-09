'''
Basic Calculator
Date Created: 10-26-19
Author: Madie Struwe

This file with be a basic calulatr
and will be able to do the following:
-addition
-subtraction
-multiplicaton
-divison
'''
#global variables for our math
global x
global y
global selection

#this function does additon
#takes 2 inputs, x and y
#returns the sum of the two numbers
def add(x, y):
    return float(x) +float(y)

#this function does subtraction
#takes 2 inputs, x and y
#returns the difference of the two numbers
def sub(x, y):
    return float(x) - float(y)

#this function does multiplication
#takes 2 inputs, x and y
#returns the product of the two numbers
def mult(x, y):
    return float(x) * float(y)

#this function does divison
#takes 2 inputs, x and y
#returns the quotient of the two numbers
def div(x, y):
    return float(x) / float(y)

#function to take input numbers from user
#and then do the selected operation
def do_math(selection):
    if selection == '1':
        x = input ("Please enter the first value:")
        y = input ("Please enter the second value:")
        print (x, "+", y, "=",add(x, y))
        menu()
    elif selection == '2':
        x = input ("Please enter the first value:")
        y = input ("Please enter the second value:")
        print (x, "-", y, "=",sub(x, y))
        menu()
    elif selection == '3':
        x = input ("Please enter the first value:")
        y = input ("Please enter the second value:")
        print (x, "*", y, "=",mult(x, y))
        menu()
    elif selection == '4':
        x = input ("Please enter the first value:")
        y = input ("Please enter the second value:")
        if y == '0':
            print ("Cannot Divide By Zero")
            menu()
        else:
            print (x, "/", y, "=",div(x, y))
            menu()
    elif selection =='5':
        print ("Thank you for using the BasicCalculator")
    else:
        print ("Please enter a valid option")
        menu()

#this is the main menu
#displays the options to the user
#then calls the do_math to do math
def menu():
    print ("Options \n")
    print ("1: Additon \n")
    print ("2: Subtraction \n")
    print ("3: Multiplication \n")
    print ("4: Divison \n")
    print ("5: Quit The Application \n")
    selection = input ("Please Pick an Operation: ")
    #call function to do math
    do_math(selection)

#print welcome message
print("Welcome to the BasicCalculator! \n \
This Application can add two numbers, \
subtract two numbers, multiply two numbers, \
or divide two numbers \
\n Author: Madie Struwe")
#call the menu function
menu()
