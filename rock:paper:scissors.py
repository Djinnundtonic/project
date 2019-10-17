#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 22:06:15 2019

@author: djinn
"""
print("warp 6")
print("Winning Rules of the Rock paper scissor game as follows: \n + " "rock vs scissors---> rock" "\n +" " rock vs paper -> paper" "\n +"" paper vs scissors -> scissors")
while True: 
    print ("Enter Choice" "\n" "1.Rock""\n""2. Scissors" "\n" "3. Paper \n" )
    choice = int (input ("user turn:"))
while choice >3 or choice <1:
    choice = int(input (" enter valid input:"))
if   choice ==1:
    choice_name = 'Rock'
elif choice ==2:
    choice_name = "scissors"
else:
    choice_name = "Paper"

print("user choice is: " + choice_name)
print("\nNOw its the computer turn....")