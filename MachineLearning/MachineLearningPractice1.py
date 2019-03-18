from sklearn import tree
# Machine learning practice 1
features = [[250, 1], [300, 1], [400, 0], [600, 0]]
labels = [1, 0, 1, 0,]

# Functions
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features,labels)

print (clf.predict([[400, 0]]))
