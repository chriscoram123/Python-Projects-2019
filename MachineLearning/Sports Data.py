import matplotlib.pyplot as plt
import numpy as np
from pygorithm import sorting
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 13 00:53:50 2019
@author: christophercoram
"""
# Use sorting to organize the amount of players on the team in order by they're jersey number.
##########################
playerNumbers = [32, 57, 23, 16, 56, 4, 1, 24]
# Class holds functions related to sorting
class sort():
 # Sorting function aranges playerNumbers variable from least to greatest
 def sortingPlayers(self):
     for i in range(len(playerNumbers)):
      sorting.bubble_sort.sort(playerNumbers)
      
      # objectx variable contains class sort() to call function
objectx = sort()

# Instructions on how to access sorting function in class
print("To organize player numbers, input Arange: ")
x = input()
def execute():
    # If statement allows user input to call class
    if x == "Arange":
        objectx.sortingPlayers()
        print("*************")
# execute function allows user input on console
execute()



# Create two charts displaying fanbase opinions over players:
##########################
# Bar chart predicting player scores for tonights game
##########################
N = 8
playerPointNumbers = (30, 22, 3, 19, 26, 8, 13, 14)
width = 0.35
ind = np.arange(N)
# Class holds functions related to pygorithm
class graphOne():
    # playerPoints function will gather data from variable and diplay a 2D chart in console
 def playerPoints(self): 
        p1 = plt.bar(ind, playerPointNumbers, width,) 
    
        plt.title('Predicted Scores For Tonights Game, 2019')
        plt.xticks(ind, ('Rondo','Kobe','Shaq','Curry','Durrant','Jordan','CP3','Westbrook'))
        plt.yticks(np.arange(0, 50, 20))
        plt.xlabel("Players")
        plt.ylabel("Predicted Scores")
        plt.legend((p1[0], ('Players')))
        plt.show
 # objecty variable contains class graphOne() to call function
objecty = graphOne()
# Instructions on how to access plt conditions in class
print("To bring up both charts, follow instructions.")
print("input Graph One: ")
x = input()
def executeTwo():
    # If statement allows user input to call class
    if x == "Graph One":
        objecty.playerPoints()
        print("*************")
# execute function allows user input on console
executeTwo()



# Bar Chart of fan opions on most favorite / valuable players
##########################
# Fixing random state
np.random.seed(19680801)
plt.rcdefaults()
fig, ax = plt.subplots()
# Bar chart data
players = ('Rondo','Kobe','Shaq','Curry','Durrant','Jordan','CP3')
y_pos = np.arange(len(players))
playerNames = 3 + 10 * np.random.rand(len(players))
error = np.random.rand(len(players))
class graphTwo():
 def favoritePlayers(self):
        ax.barh(y_pos, playerNames, xerr=error, align='center', 
                color='green', ecolor='green')
        ax.set_yticks(y_pos)
        ax.set_yticklabels(players)
        ax.invert_yaxis() 
        ax.set_xlabel('Favoriblity Rating Out Of Twelve')
        plt.ylabel("Player Names")
        ax.set_title('Most Valuable / Favorite Player, 2019')
        plt.show()
# objectz variable contains class graphTwo() to call function
objectz = graphTwo()
# Instructions on how to access plt conditions in class
print("input Graph Three: ")
x = input()
def executeThree():
    # If statement allows user input to call class
    if x == "Graph Three":
        objectz.favoritePlayers()
        print("*************")
# execute function allows user input on console       
executeThree()
