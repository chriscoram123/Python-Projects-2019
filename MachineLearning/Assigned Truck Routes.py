from pygorithm import sorting
from sklearn import tree
# Pygorithm will use sorting bubble to organize route miles from shortest 
# distance to longest distance.
# ML will take routeMiles then assign them to trucks 1, 2, 3, and 4 at random.

# Arrays for truck numbers and routeMiles
trucks = [[1, 3], [2, 1], [3, 4], [4, 2]]
routes = [1, 2, 3, 4]
routeMiles = [350, 450, 800, 120]


def organize():  # organize route miles
    for i in range(0, 4):
        sorting.bubble_sort.sort(routeMiles)
        return routes


features = trucks  
labels = routes

def assign():  # assign routes at random to each truck
        clf = tree.DecisionTreeClassifier()
        clf = clf.fit(features, labels)
        print(clf.predict([[1, 3],[4, 2],[1, 3],[3, 4]]))
 
       
organize()
assign()