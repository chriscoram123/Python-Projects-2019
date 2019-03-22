from sklearn import tree

feet = [20, 70, 30, 80, 5, 9, 60]
# 1 = Up and 2 = Down in features variable
features = [[1, feet[0]], [0, feet[1]], [1, feet[2]], [0, feet[3]], [1, feet[4]], [0, feet[5]], [1, feet[6]]]
label = [1, 0]  # 1 = Increase and 2 = Decrease

# Classifier
clf = tree.DecisionTreeClassifier()
clf.fit(features, label)


print(clf.predict([1, feet[0]]))
