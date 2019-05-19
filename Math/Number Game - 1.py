from pygorithm import sorting
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May 18 02:47:02 2019

@author: christophercoram
@title: User-Input-Number-Game
"""
print("Instructions: Welcome to my number game. The main objective to beating the following two challenges are listed below...")
number_line = [10, 15, 30, 20, 2, 8]
# Class section 1  will instruct players to guess a number between 20 and 30.
# If the guess matches if input, then number_line will organize from least to greatest
# If the player guesses wrong, the script for the game will cease function    
class SectionOne():
    def instructions(self):
        print("Before you can advance, you need to organize our number line. 10, 15, 30, 20, 2, 8.")
        print("To organize our number line, guess a number between 20 and 30")
   
# Store SectionOne Class into object_x variable   
object_x = SectionOne()

x = input()
while True:
 # Challenge one with instructions will display first
  object_x.instructions()
  if x == "25":
        print("Congrats! You won round one :)")
        sorting.bubble_sort.sort(number_line)
        continue
  else:
        print("Sorry, you lost challengeOne :(")
        break

# Class section 2 will instruct players to guess three numbers between the intervals of the number line given.
# If player guess matches the three if inputs, then player will win the game
# If player guesses wrong inputs, then the script in the game will cease function
class SectionTwo():
    def instructionsTwo(self):
        print("ChallengeTwo Instructions: Now that you have your number line, it's time to guess three numbers between three intervals. 2 and 8, 8 and 15, 15 and 20.")
        print("Example: 6, 9, 11")
# Store SectionTwo class into object_y variable          
object_y = SectionTwo()
       
x = input()      
while True:
 # Instructions for challenge two will display second
  object_y.instructionsTwo()
  if input == "4, 12, 18":
        print("Congrats! You won round two :)")
        continue
  else:
        print("Sorry, you lost challengeTwo :(")
        break
        
