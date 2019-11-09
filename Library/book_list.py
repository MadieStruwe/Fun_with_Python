'''
list.py
Library Managment System
Date Created: 11-8-19
Author: Madie Struwe

This file will read in the data in the
'Inventory.txt' and Split it based on
the book name, author, and how many are 
in the system
'''

def book_list():
    global bookname
    global authorname
    global quantity
    bookname=[]
    authorname=[]
    quantity=[]
    #open the inventory list
    with open("Inventory.txt","r") as b:
        #read line by line
        lines=b.readlines()
        lines=[x.strip('\n') for x in lines]
        #iterate through every line
        for i in range(len(lines)):
            ind=0
            #recognise that ',' indicates new data
            for a in lines[i].split(','):
                #the first piece of data is the book name
                if(ind==0):
                    bookname.append(a)
                #the second piece if data is the authors name
                elif(ind==1):
                    authorname.append(a)
                #the third piece of data is the quantity the library has
                elif(ind==2):
                    quantity.append(a)
                #after i see where i am in the line, move to the next piece
                ind+=1
                
