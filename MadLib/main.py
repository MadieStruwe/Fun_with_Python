'''
main
Date Created: 10-27-19
Author: Madie Struwe

This file will be the main file
for the MadLibs app. In order
to run the app, this file must be 
run.
'''

#import the other files
import menu as m1

#the main program. 
#nothing much in it besides function calls
def main():
    #Welcome the user when the program is started up
    print ("Welcome to MadLibs! \n\
Author: Madie Struwe")
    #ask them if they want to play
    #by calling the menu file
    m1.ask_for_help()

#run the program
main()

