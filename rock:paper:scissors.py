#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 22:06:15 2019

@author: djinn
"""
import random
playAgain = True #playagain=true keep as a means to force an outcome to spin 
print("warp 6")
print("Winning Rules of the Rock paper scissor game as follows: \n + " "rock vs scissors---> rock" "\n +" " rock vs paper -> paper" "\n +"" paper vs scissors -> scissors")
while playAgain: 
    
    print ("Enter Choice" "\n" "1. Rock""\n""2. Scissors" "\n" "3. Paper \n" )
    choice = int (input ("User turn:"))
    while choice >3 or choice <1:
        choice = int(input (" enter valid input:"))
    if   choice == 1:
        user_choice = 'Rock'
    elif choice == 2:
        user_choice = 'Scissors'
    else:
        user_choice = 'Paper'
    
    print("User choice is: " + user_choice)

     
    print( "\nSkynet is priming")
      #not sure why values that are equal are ==
      # Computer chooses randomly any number  1
        # among 1 , 2 and 3. Using randint method 
        # of random module 
    comp_choice = random.randint (1,3)
    if  comp_choice == 1: 
        choice_name = 'Rock'
    elif comp_choice == 2: 
        choice_name = 'Scissor'
    else :
        choice_name = 'Paper'
    print("Computers choice: ", choice_name)
    
    # Evaluation
    if choice == 1 and comp_choice == 3:
        print ("<==Skynet wins!==>")
   #choice is == to number (choice_name == to string)
    elif choice == 1 and comp_choice == 2:
        print ("<==User wins==>")
    elif choice == 2 and comp_choice == 1:
        print ("<==Skynet wins==>!")
    elif choice == 2 and comp_choice == 3:
        print (" <==User wins==>")
    elif choice == 3 and comp_choice == 1:
        print ("<==User wins==>")
    elif choice == comp_choice:            a
        print ("<==Tie==>")
    elif choice == 3 and comp_choice == 2:
        print ("<==Skynet wins!==>")
          # Printing either user or computer wins 
    
        
    
    
    print ("Do you want to play again?(Y/N)")
    ans = input()
    if ans == ("y") or ans == ("Y"):
        print ("\n Really again? ;)")
    if ans == ("n") or ans == ("N"):
        print ("\n Thank you for Playing!")
        playAgain = False
    #break   
    
    