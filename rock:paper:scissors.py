#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 22:06:15 2019

@author: djinn
"""
import random
print("warp 6")
print("Winning Rules of the Rock paper scissor game as follows: \n + " "rock vs scissors---> rock" "\n +" " rock vs paper -> paper" "\n +"" paper vs scissors -> scissors")
while True: 
    
    print ("Enter Choice" "\n" "1. Rock""\n""2. Scissors" "\n" "3. Paper \n" )
    choice = int (input ("User turn:"))
    while choice >3 or choice <1:
        choice = int(input (" enter valid input:"))
    if   choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'Scissors'
    else:
        choice_name = 'Paper'
    
    print("User choice is: " + choice_name)

     
    print( "\nSkynet is priming")
      #not sure why values that are equal are ==
      # Computer chooses randomly any number  
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
    if choice_name == 1 and comp_choice == 3:
        print ("Skynet wins!")
   
    elif choice_name == 1 and comp_choice == 2:
        print ("User wins")
    elif choice_name == 2 and comp_choice == 1:
        print ("Skynet wins!")
    elif choice_name == 2 and comp_choice == 3:
        print (" User wins")
    elif choice_name == 3 and comp_choice == 1:
        print ("User wins")
    elif choice_name == comp_choice:            
        print ("Tie")
    elif choice_name == 3 and comp_choice == 2:
        print ("Skynet wins!")
          # Printing either user or computer wins 
    if choice_name == choice_name or choice_name == comp_choice: 
        print("<==Skynet Wins==>") 
    else: 
        print("<== Skynet wins ==>") 
        
    
    
    print ("Do you want to play again?(Y/N)")
    ans = input()
    if ans == ("y") or ans == ("Y"):
        print ("\n Really again? ;)")
    if ans == ("n") or ans == ("N"):
        print ("\n Thank you for Playing!")
    break    
    
    