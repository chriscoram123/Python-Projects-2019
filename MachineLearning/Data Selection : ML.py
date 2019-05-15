from sklearn import tree

class labeling():
	features = [[],[],[],[]]
	labels = [1,0,1,0]
	inst = "Labeling data from function one."
	def function():
		clf = tree.DecisionTreeClassifier()
		clf = clf.fit(features, labels)
		print(clf.predict())

	featuresTwo = [[],[],[],[]]
	labelsTwo = [1,0,1,0]
	instTwo = "Labeling data from function two."
	def functionTwo():
		clf = tree.DecisionTreeClassifier()
		clf = clf.fit(featuresOne, labelsTwo)
		print(clf.predict())
myobjectx = labeling()


def execution():
N = input("Label One")
J = input("Label Two")
while N == "Label One":
	print(myobjectx.inst)
	myobjectx.function()
	break

while J == "Label Two":
	print(myobjectx.instTwo)
	myobjectx.functionTwo()
	break


execution()