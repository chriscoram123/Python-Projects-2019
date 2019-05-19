from pygorithm import sorting
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 18 02:47:02 2019

@author: christophercorame
@title: User-Input-Number-Game
"""
print("Instructions: Welcome to my number game. The main objective to beating the following two challenges are listed below...")
number_line = [10, 15, 30, 20, 2, 8]
# Class section 1  will instruct players to guess a number between 20 and 30.
# If the guess matches if input, then number_line will organize from least to greatest
# If the player guesses wrong, the script for the game will cease function    
print("Before you can advance, you need to organize our number line. 10, 15, 30, 20, 2, 8.")
print("To organize our number line, guess a number between 20 and 30")

x = input("Enter your number:")
def exe():
 # Challenge one with instructions will display first
 if x=="25":
  for i in range(0, 3):
        sorting.bubble_sort.sort(number_line)
        print("Congrats! You won round one: Press Enter")
        return range
# execute function allows user input on console
exe()


# Class section 2 will instruct players to guess three numbers between the intervals of the number line given.
# If player guess matches the three if inputs, then player will win the game
# If player guesses wrong inputs, then the script in the game will cease function
print("ChallengeTwo Instructions: Now that you have your number line, it's time to guess three numbers between three intervals. 2 and 8, 8 and 15, 15 and 20.")
print("Example: 6, 9, 11")
  
x = input("Enter your number:")      
def exeTwo():
 # Instructions for challenge two will display first
  if x == "4, 12, 18":
        print("Congrats! You won round two:")
# execute function allows user input on console
exeTwo() 

