from sklearn import tree
# Machine Learning will indicate who has the higest credit score among the 5 individuals stated
# Credit Card Ints... Chase = 11 / Discover = 23 / Bank of America = 35 / TD Bank = 46
# Label Ints... Joe = 1 / Amina = 2 / Henry = 3 / Thor = 4

score = [650, 790, 200, 800] # Array for credit scores
feature = [[11, score[0], [23, score[1]], [35, score[3]], [46, score[2]]]          
label = [1, 2, 3, 4]

# Functions
clf = tree.DecisionTreeClassifier()
clf = clf.fit(feature,label)

print(clf.predict([[11, score[0]])
