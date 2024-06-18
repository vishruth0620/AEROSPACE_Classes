#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 00:10:27 2020

@author: vishruth
"""
# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Name: Vishruth Balaji, Hunter Spier, Michael Camacho, Liliana Salgado
# Course Header: Eng 102-451
# Assignment: Lab 7a Activity 3
# Date: 9/28/2020

###Instructions for User Input###
#Step 1: Select a starting position by entering a starting row and column value to the console
#Step 2: Select an ending position by entering an ending row and column value to the console
#Step 3: If you want to stop the game, enter stop on question when it asks the starting row

#Create a 8 X 8 chessboard using a list variable chessBoard
chess_Board = [
['R','N','B','Q','K','B','N','R'],
['P','P','P','P','P','P','P','P'], 
['.','.','.','.','.','.','.','.'],
['.','.','.','.','.','.','.','.'],
['.','.','.','.','.','.','.','.'],
['.','.','.','.','.','.','.','.'],
['p','p','p','p','p','p','p','p'],
['r','n','b','q','k','b','n','r']]

#Print each row of the list chessBoard
for row in range(len(chess_Board)):
    print(chess_Board[row])

#Output to start the chess match
print('\nStart the game!')

#Iterate the game and moves by players using a while loop that sets the conditional to true
while (True):
    
    #Input a Starting row number from 0 to 7
    starting_Row = input('Enter the starting row position (0-7): ')
    
    #Check if user entered stop
    #If true, then break out from the while loop
    if(starting_Row == 'stop'):
        print('\nThanks for playing!')
        break
    
    #Convert the string number to an integer
    #Set inputs for the Starting Column, Ending Row and Ending Column
    starting_Row = int(starting_Row)
    starting_Column = int(input('Enter the starting column position (0-7): '))
    ending_Row = int(input('Enter the ending row position (0-7): '))
    ending_Column = int(input('Enter the ending column position (0-7): '))
    
    #Check if any of the inputs of rows and columns are between 0 to 7 
    #If true, then iterate to the next if statment
    #Else, print an invalid position and try again
    if((0 <= starting_Row <= 7) and (0 <= starting_Column <= 7) and (0 <= ending_Row <= 7) and (0 <= ending_Column <= 7)):
        
        #Checking if the starting row and column has no piece
        #If there is, then try another starting and ending positions
        if(chess_Board[starting_Row][starting_Column] == '.'):
            print('\nThere is no piece to move, Try Again!')
        
        
        else:
            
            #Move the starting position of row and column to the ending position of row ans column 
            chess_Board[ending_Row][ending_Column] = chess_Board[starting_Row][starting_Column]
            
            #Replace the starting row and column with a period
            chess_Board[starting_Row][starting_Column] = '.'
            
            #Print the updated cheesBoard after each move using the for loop 
            for row in range(len(chess_Board)):
                print(chess_Board[row])
    else:
        print('\nThis is an invalid position, Try Again!')
    