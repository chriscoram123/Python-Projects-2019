# Python practice1, user input and usage of arrays

# (color1)variable group 1
Red = ['259' '683']  # Numerical group 1
Blue = ['469' '348']  # Numerical group 2
Green = ['699' '888']  # Numerical group 3
# (color2)
Yellow = ['259' '683']  # Numerical group 4
Pink = ['469' '348']  # Numerical group 5
Purple = ['699' '888']  # Numerical group 6

# Variable group 2
option1 = ['Red' 'Blue' 'Green']  # Variable group for color1
option2 = ['Yellow' 'Pink' 'Purple']  # Variable group for color2
option3 = 0  # null variable
option4 = 1  # elif variable
collective = ['option1' 'option2']

# conditions
Q = Red  # variable group 1
W = Blue  # variable group 1
E = Green  # variable group 1
A = Yellow  # variable group 2
S = Pink  # variable group 2
D = Purple  # variable group 2
option1_onscreen_1 = Q  # When input in console, variable 'Q' will
#  connect to option 1

option1_onscreen_2 = input(W)  # When input in console, variable 'Q' will
# connect to option 2

option1_onscreen_3 = input(E)  # When input in console, variable 'Q' will
# connect to option 3

option1_onscreen_4 = input(A)  # When input in console, variable 'Q' will
#  connect to option 1

option1_onscreen_5 = input(S)  # When input in console, variable 'Q' will
# connect to option 2

option1_onscreen_6 = input(D)  # When input in console, variable 'Q' will
# connect to option 3


def onscreen():
 print("CHOOSE ONE OF THE FOLLOWING INPUTS...'Q','W','E','A','S','D'")
# Six if statements
 if option1_onscreen_1 == Q:  # User execution
   for x in Red:
       print(x)

 if option1_onscreen_2 == W:  # User execution
   for x in Blue:
       print(x)

 if option1_onscreen_3 == E:  # User execution
   for x in Red:
       print(x)

 if option1_onscreen_4 == A:  # User execution
   for x in Red:
       print(x)

 if option1_onscreen_5 == S:  # User execution
   for x in Red:
       print(x)

 if option1_onscreen_6 == D:  # User execution
   for x in Red:
       print(x)


def onscreen2():
 print("CHOOSE ONE OF THE FOLLOWING INPUTS TO DISPLAY ON CONSOLE...")
#  Two if statements
 if option3 == 0:
   print(option1, "YOU LIKE THESE OPTIONS!")  # User execution

 elif option4 == 1:
     print(option2, "YOU LIKE THESE OPTIONS INSTEAD!")  # User execution
 

# Definition execution
onscreen()
onscreen2()
