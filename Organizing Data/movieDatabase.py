"""
  movieDatabase.py - User input system to store selection in movies in dictionairies.
  Created by: Christopher S Coram
  Created on: 10052019
"""
import math
import sys

# Loop variable equals true
running = True

# Dictionaries will store all results from user input operations
movie_Genres = ["Horror", "Sci-Fi", "Comedy", "Romance", "Action"]
user_OutputGenre = []
user_OutputMovie = []
# Object x will store all clss functions
user_InputOne = input("Please select your favorite genre ")
user_InputTwo = input("Would you like to exit out the system or continue? (Y/N) ")
user_InputThree = input("Please select your favorite movie ")
user_InputFour = input("Are you finished with selection? (Y/N) ")


# Class will store all script functions
class movie_Choices:
    def __init__(self):
        print("Program loading..")

    # Displays genre question in shell
    def questionOne_System(self):
        if user_InputOne == "": # Inputs user choice
            user_OutputGenre.append(user_InputOne)
            if user_OutputTwo == "Y":
                print("Loading next question...")
            elif user_OutputTwo == "N":
                print("Exit system...")
                sys.exit()

    # Displays fav movie question in shell
    def questionTwo_System(self):
        if user_InputThree == "":
            use_OutputMovie.append(user_InputThree)
            if user_InputFour == "Y":
                print("Loading...")
            elif user_InputFour == "N":
                print("Exit system...")
                sys.exit()
        
object_x = movie_Choices()

# Run script
object_x.questionOne_System()
object_x.questionTwo_System()


