import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error,r2_score

# Load Dataset
diabetes = datasets.load_diabetes()

# Train / Test X Data
diabetes_x = diabetes.data[:,np.newaxis,2]
diabetes_x_train = diabetes_x[:-30] # Splitting Targets Into Training And Test Sets
diabetes_x_test = diabetes_x[-30:]

# Train / Test Y Data
diabetes_y_train = diabetes.target[:-30] # Splitting Targets Into Training And Test Sets
diabetes_y_test = diabetes.target[-30:]

# Setup Linear Regression
regr = linear_model.LinearRegression()  # Linear Regression Object
regr.fit(diabetes_x_train,diabetes_y_train)  # Use Training Sets To Train Model


# Plot Layout
diabetes_y_pred = regr.predict(diabetes_x_test) # Make Predictions
regr.coef_

mean_squared_error(diabetes_y_test,diabetes_y_pred) 

r2_score(diabetes_y_test,diabetes_y_pred) # Variance Score

plt.plot(diabetes_x_test,diabetes_y_pred,color = 'pink', linewidth =3) # Plot Linear Data

plt.scatter(diabetes_x_test,diabetes_y_test, color = 'lavender')

plt.plot(diabetes_x_test,diabetes_y_pred, color = 'pink', linewidth = 3)


# Execute Functions
plt.xticks(())

plt.yticks(())

plt.show()