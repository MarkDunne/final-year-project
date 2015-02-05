import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.neighbors import KNeighborsRegressor
from sklearn.neighbors import KNeighborsClassifier
from sklearn.grid_search import GridSearchCV
from sklearn.cross_validation import KFold
from sklearn.cross_validation import train_test_split
from sklearn.metrics import classification_report

data_loc = '/home/mark/workspace/final-year-project/data/machines/DJIA-window-history.csv'

data = pd.DataFrame.from_csv(data_loc)
estimator = KNeighborsClassifier(n_neighbors=100)

X = data[[0, 1, 2, 3, 4]].values
y = data[['outcome-class']].values.ravel()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1)

print 'test size:', len(X_test)

estimator.fit(X_train, y_train)
y_predicted = estimator.predict(X_test)

print classification_report(y_test, y_predicted)