import numpy as np
from sklearn import tree
import matplotlib.pyplot as plt
# Initiate 2D bargraph on command 
# Initiate ML to label which states have the most major and minor cases overall
N = 5
menDiabetes = (250, 560, 320, 456, 135)
diagnosis = (1, 2, 3, 4, 5)
ind = np.arange(N)
width = 0.05

def diabetes():
	i = input("One")
	while i == "One":
     p1 = plt.bar(ind, menDiabetes, width, yerr = )
     plt.title("Diabetic Rates For Men In Five States/2018")
     plt.xlabel("States")
     plt.ylabel("Amount of Dibetic Patients")
     plt.xticks(ind, ("Chicago", "New York", "Boston", "Maryland", "Iowah"))
     plt.yticks(np.arrange(0, 600, 300))
     plt.show()
	 break


def identification():
	features = [[250, 0], [560, 1], [320, 0], [456, 1], [135, 0]]
	labels = [1, 0]
	j = input("Two")
	while j == "Two":
		clf = tree.DecisionTreeClassification()
		clf = clf.fit.(features, labels)
        print(clf.predict([[250, 0], [560, 1], [320, 0], [456, 1], [135, 0]]))
        break


diabetes()
identification()