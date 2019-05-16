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
playerNumbers = [32, 57, 23, 16, 56, 4, 1, 24]
N = input("To organize player numbers, type arange: ")
class sort():
 def sortingPlayers():
    while N == "arange":
        for i in range(len(playerNumbers)):
            sorting.bubble_sort.sort(playerNumbers)
myobjectx = sort()
print("Data 1", myobjectx.sortingPlayers())



# Create two charts displaying fanbase opinions over players
# Bar chart predicting player scores for tonights game
N = 5
playerPointNumbers = (30, 22, 3, 19, 26, 8, 13, 14)
playerSt = (2,3,4,1,2)
width = 0.25
ind = np.arange(N)
def playerPoints():
    J = input("Predicted Score Chart")
    print("For player score bar chart, input + J")
    while J == "Predicted Score Chart":
        
        p1 = plt.bar(ind, playerPointNumbers, width, yerr=playerSt) 
    
        plt.title('Predicted Scores For Tonights Game, 2019')
        plt.ylabel('Player Points')
        plt.xlabel('Player Jersey Numbers')
        plt.xticks(ind, ('Rondo','Kobe','Shaq','Curry','Durrant','Jordan','CP3'))
        plt.yticks(np.arange(0, 50, 20))
        plt.legend((p1[0], ('Players')))
        plt.show()
        break
    
# Bar Chart of fan opions on most favorite / valuable players
# Fixing random state
np.random.seed(19680801)
plt.rcdefaults()
fig, ax = plt.subplots()
# Bar chart data
players = ('Rondo','Kobe','Shaq','Curry','Durrant','Jordan','CP3')
y_pos = np.arange(len(players))
playerNames = 3 + 10 * np.random.rand(len(players))
error = np.random.rand(len(players))
def favoritePlayers():
    J = input("Favorite Players")
    print("For player score bar chart, input + J")
    while J == "Favorite Players":
        ax.barh(y_pos, playerNames, xerr=error, align='center', 
                color='green', ecolor='black')
        ax.set_yricks(y_pos)
        ax.set_yticklabels(players)
        ax.invert_yaxis() 
        ax.set_xlabel('playerNames')
        ax.set_title('Most Valuable / Favorite Player, 2019')
        plt.how()
        break


playerPoints()
favoritePlayers()