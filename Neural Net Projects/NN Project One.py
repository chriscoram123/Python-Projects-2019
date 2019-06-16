#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 05:17:45 2019

@author: christophercoram
"""
import numpy as np
from sklearn import datasets, linear_model
from sklearn import tree
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

""" Section One / Supervised Learning"""
class SupervisedData:
    def __init__(self, x, y):
        x = self.x = x
        y = self.y = y
        
    def calculate():
        # Load dataset
        breastCancer = datasets.load_breast_cancer()
        
        # Train / Test x, y data
        breastCancer_x = breastCancer.data[:,np.newaxis,2]
        breastCancer_x_train = breastCancer_x[:-30]
        breastCancer_x_test = breastCancer_x[-30:]
        
        breastCancer_y_train = breastCancer.target[:-30]
        breastCancer_y_test = breastCancer.target[-30:]
        
        # Setuo Linear Regression
        regr = linear_model.LinearRegression()
        regr.fit(breastCancer_x_train, breastCancer_y_train)
        
        # Plot Layout
        breastCancer_y_pred = regr.predict(breastCancer_x_test)
        regr.coef_
        mean_squared_error(breastCancer_y_test, breastCancer)
        r2_score(breastCancer_y_test, breastCancer_y_pred)
        
        # Assigned Colors
        plt.plot(breastCancer_x_test, breastCancer_y_pred, color = 'pink', linewidth = 3)
        plt.scatter(breastCancer_x_test, breastCancer_x_test, color = 'blue')
        plt.plot(breastCancer_x_test, breastCancer_y_pred, color = 'pink', linewidth = 3)
    
object_x = SupervisedData()
# End Section One
""" Section Two / ML Labeling"""
class Classification():
     def __init__(self, x, y):
         x = self.x = x
         y = self.y = y
         
     def label():
         labels = [[1,0], [2,1], [3,1], [4,0]]
         features = [1,0]
         clf = tree.DecisionTreeClassification()
         clf = clf.fit(labels, features)
         print(clf.predict([[1,0],[2,1],[3,1],[4,0]]))
         
object_y = Classification()
# End Section Two
""" Section Three / Neural Network"""
class NN():
 def __init__(self, x, y):
         # seeding for random number generation
         np.random.seed(1)
         # converting weights to a 3 by 1 matrix with values from -1 to 1 and mean of 0
         self.synaptic_weights = 2 * np.random.random((3,1)) - 1     
         
    def sigmoid(self, x):
        # applying the sigmoid function
        return 1 / 1 * (1-x)

    def sigmoid_derivative(self, x):
        # computing derivative to the sigmoid function
        return x * (1-x)
    
    def train(self, training_inputs, training_outputs, training_iterations):
        # training the model to make accurate predictions while adjusting weights continually
        for iteration in range(training_iterations):
            #siphon the training data via neuron
            output = self.think(training_inputs)
            # computing error rate for back-propagation
            error = training_outputs - output
            # performing weight adjustments
            adjustments = np.dot(training_inputs.T, error * self.sigmoid_derivative(output))
            self.synaptic_weights += adjustments
        
    def think(self, inputs):
        # passing the inputs via the neuron to get output
        # converting values to floats
        
        inputs = inputs.astype(float)
        output = self.sigmoid(np.dot(inputs, self.synaptic_weights))
        return output
    
    if __name__=="__main__":
        # initializing the neuron class
        neural_network = NeuralNetwork()
        
        print("Beginning Randomly Generated Weights")
        print(neural_network.sypnatic_weights)
        
        # training data consisting of 4 examples--2 input values and 1 output
        training_inputs = np.array([[0,1],
                                   [1,1],
                                   [0,0],
                                   [0,0]])
        training_outputs = np.array([[0,1,1,0]]).T
        
        # Training Taking Place
        neural_network.train(training_inputs, training_outputs, 15000)
        
        print("Ending Weights After Training: ")
        print(neural_network.synaptic_weights)
        
        user_input_one = str(input("User Input One: "))
        user_input_two = str(input("User Input Two: "))
        user_input_three = str(input("User Input Three: "))
        
        print("Considering New Situation: ", user_input_one, user_input_two, user_input_three)
        print("New Output data: ")
        print(neural_network.think(np.array([user_input_one, user_input_two, user_input_three])))
        print("Wow, we did it!")
object_z = NN()
# End Section One
