
# Variables containing equations that are related to student attendance
# information.
equationYearly = 365 * 5  # equation1
equationHolidays = 45 * 5  # equation2
equationDaysOff = 20 * 5  # equation3
# Containers for inputs
equationOne = 365  # Input container 1
equationTwo = 45  # Input container 2
equationThree = 20  # Input container 3
# Conditions
Input_1 = input(equationOne)
Input_2 = input(equationTwo)
Input_3 = input(equationThree)

winter = 3 * 5
fall = 3 * 5

print("STUDENT ATTENDANCE")  # Prints input title on console


#  Functions
def subject1():
 if Input_1 == equationOne:  # Original amount
print("DAYS PER YEAR * FIVE YEAR SPAN, COMPARED TO MONTHS IN WINTER/FALL * FIVE YEAR SPAN.")
#  Compares multiple of five to original
print('Days per year', equationYearly)
print('Average months per winter', winter)
print('Average months per fall', fall)


def subject2():
 if Input_2 == equationTwo:  # Original amount
print("HOLIDAYS PER YEAR * FIVE YEAR SPAN, COMPARED TO DAYS PER YEAR * FIVE YEAR SPAN.")
#  Compares multiple of five to original
print('Days per year', equationYearly)
print('Holidays per year', equationHolidays)


def subject3():
 if Input_3 == equationThree:  # Original amount
print("DAYS OFF PER YEAR * FIVE YEAR SPAN, COMPARED TO DAYS PER YEAR * FIVE YEAR SPAN.")
#  Compares multiple of five to original
print('Days per year', equationYearly)
print('Holidays per year', equationDaysOff)


subject1()
subject2()
subject3()
