from pygorithm import sorting
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error,r2_score
import matplotlib.pyplot as plt
import numpy as np

# Load Dataset
breastCancer = datasets.load_breast_cancer()

# Train / Test X, Y Data
breastCancer_x = breastCancer.data[:,np.newaxis,2]
breastCancer_x_train = breastCancer_x[:-30]
breastCancer_x_test = breastCancer_x[-30:]

breastCancer_y_train = breastCancer.target[:-30]
breastCancer_y_test = breastCancer.target[-30:]

# Setup Linear Regression
regr = linear_model.LinearRegression()
regr.fit(breastCancer_x_train, breastCancer_y_train)

# Plot Layout
breastCancer_y_pred = regr.predict(breastCancer_x_test)
regr.coef_
mean_squared_error(breastCancer_y_test,breastCancer_y_pred)
r2_score(breastCancer_y_test,breastCancer_y_pred)

# Assigned Colors
plt.plot(breastCancer_x_test,breastCancer_y_pred, color = 'pink', linewidth = 3)
plt.scatter(breastCancer_x_test,breastCancer_y_test, color = 'blue')
plt.plot(breastCancer_x_test,breastCancer_y_pred, color = 'pink', linewidth = 3)


# Patient Variables
patients = [140, 80, 120, 60, 100]
def arangePatients():
	for i in range(0, 5):
		sorting.bubble_sort.sort(patients)
		print("Total amount of patients in hospital = 500")
		return arangePatients

    

# Instructions for reader
def instructions():
    print("Instructions for Y Axis: 1 = Critical Breast Cancer patients, 0 = Non critical diabetic patients")
    print("Instructions for X Axis: wing1 = 60, wing2 = 80, wing3 = 100, wing4 = 120, wing5 = 140")
    print('------------------------------')
    print("As you can see, there is a higher concentration of critical patients in Wings 1 through 3. Compared to Wings 4 through 5, which have a lower concentration of non critical patients. ")
    print("Stating that Wings 1 through 3 have the higest amount of critical breast cancer patients in 2019 in Hypothetical Hospital.")
    
# Execute Plot Functions
plt.title('Breast Cancer Status 2019, Hypothetical Hospital ')
plt.ylabel('Critical Status of Breast Cancer Patients')
plt.xlabel('Number of Patients In Each Hospital Wing')
plt.yticks(np.arange(0, 1.5, 1))
plt.show()
# Execute Sorting Function
arangePatients()
instructions()
