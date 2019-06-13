import numpy as np
import time

InstructionOne = print("Riddle One:")
InstructionTwo = print("Math Problem:")
x = input("24")
y = input("30")
class SubsetOne():
	def Countdown(self, t):
		while t:
			mins, secs = divmod(t, 60)
			timeformat = '{:02d}:{:02d}'.format(mins, secs)
			print(timeformat, end='\r')
			time.sleep(1)
			t -= 1
		print('GAME OVER!')

object_timer = SubsetOne()


class LevelOne():
	def __init__(self, x, y,):
		x = self.x = x
		y = self.y = y

	def ObsticleOne(self):
		print(InstructionOne)
		if x == input("24"):
			object_timer.Countdown()
			i = input("Pie")
			print("You have activated timer: Solve before the clock hits zero! ")
			print("Riddle One: ")
			if i == input("Pie"):
				print("Press ENTER to continue:")
			else:
				print("GAME OVER: Wrong Answer")
				exit()
        else:
        	print("GAME OVER: Wrong Answer")
			exit()

object_LevelOne = LevelOne()


LevelTwoInstructions = print("")
correct1 = input("25")
class LevelTwo():
	def __init__(self, x, y,):
		x = self.x = x
		y = self.y = y

	def ObsticleTwo(self):
		print(InstructionTwo)
		if correct1 == "25":
			object_timer.Countdown()
			j = input("Snake")
			print("You have activated timer: Solve before the clock hits zero! ")
			print("Riddle Two: ")
			if j == "Snake": 
				print("Press ENTER to continue:")
			else:
				print("GAME OVER: Wrong Answer")
        	    exit()
        else:
        	print("GAME OVER: Wrong Answer")
        	exit()

object_LevelTwo = LevelTwo()


class Choices():
	def __init__(self, x, y,):
		x = self.x = x
		y = self.y = y
    
    def ChoiceOne(self):
    	print("Level One")
    	object_LevelOne.ObsticleOne()

    def ChoiceTwo(self):
    	print("Level_Two")
    	object_LevelTwo.ObsticleTwo()

object_choices = Choices()

# Player Inputs
def Game():
	e = object_choices.ChoiceOne()
	f = object_choices.ChoiceTwo()
	level_one = e
	level_two = f
	choice1 = input(level_one)
	choice2 = input(level_two)
	print("Please choose the following levels: level_one or level_two")
	if choice1 == level_one:
		print(level_one)
