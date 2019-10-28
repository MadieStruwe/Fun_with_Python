'''
menu
Date Created: 10-27-19
Author: Madie Struwe

This file will have menu options
-does the user want to play with madlibs
-if so which story

It will ask the user which story they
want to do, then call the story from
the stories.py file then ask the user
for input
'''

#import the stories file to load up selected story
import stories as st

#this function asks the user if they want 
#to run the app and play with some madlibs
#if yes, ask which story then load it
#if no, exit
#if an unexpected answer, ask again
def ask_for_help():
    #take their answer and determine yes or no
    help = input ("I need help finishing some stories. \
Can you help me? \n").lower()
    if help == 'y' or help == 'yes':
        #if yes, ask them which story
        print ("Excellent! \n \
    Here are the stories that need to be finished: \n \
        1 - Lord of the... Part 1\n \
        2 - Lord of the... Part 2\n \
        3 - Lord of the... Part 3\n \
        4 - Romeo and Juliet\n \
        5 - Dragons\n ")
        #get input on which story the user wants
        #then load that story
        story = input ("Which one would you like to finish? \n")
        load_story(story)
    elif help[:1] == 'n' or help == 'no':
        #if no, quit the program
        print ("That is unfortunite. Maybe next time.")
    else:
        print ("I'm sorry I don't understand")
        ask_for_help()

#this function is called if the user wants to
#finish a story
#based on input from the user it will load a story
#sored in stories.py
def load_story(story):
    if story == '1' or story == 'Lord of the... Part 1':
        print ("You have chosen: Lord of the... Part 1")
        st.Lord_of_the_Part_1()
    elif story == '2' or story == 'Lord of the... Part 2':
        print ("You have chosen: Lord of the... Part 2")
        st.Lord_of_the_Part_2()
    elif story == '3' or story == 'Lord of the... Part 3':
        print ("You have chosen: Lord of the... Part 3")
        st.Lord_of_the_Part_3()
    elif story == '4' or story == 'Romeo and Juliet':
        print ("You have chosen: Romeo and Juliet")
        st.Romeo_and_Juliet()
    elif story == '5' or story == 'Dragons':
        print ("You have chosen: Dragons")  
        st.Dragons()   
    #if the input is not understood, ask again
    else:
        print ("I'm sorry, I do not understand")
        ask_for_help()