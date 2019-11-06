"""
  LevelOne.py - LevelOne will contain all functions and operations related to questions and user input.
  Created by: Christopher S Coram
  Created on: 09242019
"""
import sys

#####################
##### VARIABLES #####
#####################

# Variables that relate to constructing all questions related to round one.
question_One = "SOLVE THE EQUATION: " + str(5*20)
question_Two = "SOLVE THE EQUATION: " + str(5*20+19)
question_Three = "SOLVE THE EQUATION: " + str(349+212/5)
question_Four = "SOLVE THE EQUATION: " + str(5*60-61)
question_Five = "SOLVE THE EQUATION: " + str(5-20)

# Game Score 
rd_Point = 10
maximum_Points = 50   

##########################
##### GAME QUESTIONS #####
##########################
# Class level_One will hold all round one operating features
class q_One:
  def __init__(self):
    # __init__ function for proper class setup.
    print("File running")

 # Def round_Questions will contain all of level one's questions
  def round_Questions(self):
    print("ROUND ONE")
    # input variables will contain round one questions
    input_One = input(question_One)
    # Question one if / else statements
    if input_One == "100":
      print("Correct!")
      print("Player has been awarded " + str(rd_Point))
    elif input_One == "One Hundred":
      print("Correct!")
      print("Player has been awarded " + str(rd_Point))
    else: # If player enters in wrong answer a second time
      print("Wrong! GAME OVER")
      sys.exit()

    input_Two = input(question_Two)
    # Question two if / else statements
    if input_Two == "119":
      print("Correct!")
      print("Player has been awarded " + str(rd_Point))
    elif input_One == "One Hundred Nineteen":
      print("Correct!")
      print("Player has been awarded " + str(rd_Point))
    elif input_One == "One Hundred And Nineteen":
      print("Correct!")
      print("Player has been awarded " + str(rd_Point))
    else: # If player enters in wrong answer a second time
      print("Wrong! GAME OVER")
      sys.exit()
    
    input_Three = input(question_Three)
    # Question three if / else statements
    if input_Three == "121.2":
      print("Correct!")
      print("Player has been awarded " + str(rd_Point))
    elif input_Three == "One Hundred Twenty One Point Two": # Gives player a second chance
      print("Correct!")
      print("Player has been awarded " + str(rd_Point))
    elif input_Three == "One Hundred And Twenty One Point Two": # Gives player a second chance
      print("Correct!")
      print("Player has been awarded " + str(rd_Point))
    else: # If player enters in wrong answer a second time
      print("Wrong! GAME OVER")
      sys.exit()
    
    input_Four = input(question_Four)
    # Question four if / else statements
    if input_Four == "261":
      print("Correct!")
      print("Player has been awarded " + str(rd_Point))
    elif input_Four == "Two Hundred Sixty One": # Gives player a second chance
      print("Correct!")
      print("Player has been awarded " + str(rd_Point))
    elif input_Four == "Two Hundred And Sixty One": # Gives player a second chance
      print("Correct!")
      print("Player has been awarded " + str(rd_Point))
    else: # If player enters in wrong answer a second time
      print("Wrong! GAME OVER")
      sys.exit()

    input_Five = input(question_Five)
    # Question five if / else statements
    if input_Five == "-15":
      print("Correct!")
      print("Player has been awarded " + str(rd_Point))
    elif input_Four == "Negative Fifteen": # Gives player a second chance
      print("Correct!")
      print("Player has been awarded " + str(rd_Point))
    else: # If player enters in wrong answer a second time
      print("Wrong! GAME OVER")
      sys.exit()