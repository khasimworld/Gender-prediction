# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# height, weight, shoe size
from sklearn import tree
X= [[181,80,44],[177,70,43],[160,60,38],[154,54,37],[166,65,40],[190,90,47],[175,64,39],[171,75,42],[181,85,43]]
Y=['male','female','female','male','female','female','male','male','female']
clf = tree.DecisionTreeClassifier()         #variable=clf
clf= clf.fit(X,Y)
prediction = clf.predict([[190,70,43]])

print(prediction)
