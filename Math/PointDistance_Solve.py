"""
  PointDistance_Solve.py - Python script programed to find the distance between two points.
  Created by: Christopher Coram
  Created on: 09212019
"""
# P1 = (8,-5)  P = (20,-18)  D = SquareRoot((X1 - X2)^2 + (Y1 - Y2)^2)
# All values / variables necessary to solving equation
squareRoot = 2
pointOneX = 8
pointOneY = -5
pointTwoX = 20
pointTwoY = -18
# X_Solve and Y_Solve will subtract the given point values then square root
y_Solve = pointOneX - pointTwoX ^ squareRoot
x_Solve = pointOneY - pointTwoY ^ squareRoot

# Class Distance will create / assign variable objects and give them tasks
class Distance:
    # Assign objects
    def __init__(self, pointOneX, pointOneY, pointTwoX, pointTwoY):
        self.pointOneX = pointOneX
        self.pointOneY = pointOneY
        self.pointTwoX = pointTwoX
        self.pointTwoY = pointTwoY

    # Gives objects tasks
    def solvePlot(self):
        print("Result of point one, X Y Axis Squared: " + str(x_Solve))
        print("Result of point two, X Y Axis Squared: " + str(y_Solve))
        print("Result of point one + point two: " + str(x_Solve + y_Solve))

# Assign object values to Distance class
equationResult = Distance(8,-5,20,-18)

# Run program
equationResult.solvePlot()
