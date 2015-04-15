import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.neighbors import KNeighborsRegressor
from sklearn.neighbors import KNeighborsClassifier
from sklearn.grid_search import GridSearchCV
from sklearn.cross_validation import KFold
from sklearn.cross_validation import train_test_split
from sklearn.metrics import classification_report
from plot_learning_curve import plot_learning_curve

data_loc = '/home/mark/workspace/final-year-project/data/machines/DJIA-window-history.csv'

print 'loading data'
data = pd.DataFrame.from_csv(data_loc)
estimator = KNeighborsRegressor(n_neighbors=5)

print 'reducing data'
sample = np.random.randint(len(data), size=10000)
data = data.ix[sample]

def test_classification():
    X = data[[0, 1, 2, 3, 4]].values
    y = data[['outcome-class']].values.ravel()
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1)
    
    print 'test size:', len(X_test)
    
    estimator.fit(X_train, y_train)
    y_predicted = estimator.predict(X_test)
    
    print classification_report(y_test, y_predicted)
    
def test_learning_curve():
    X = data[[0, 1, 2, 3, 4]].values
    y = data[['outcome']].values
    folds = KFold(n=len(X), n_folds=10, shuffle=True)
    fig = plot_learning_curve(estimator, "50 k-NN learning curve", X, y, cv=folds, verbose=2, 
                              train_sizes=np.linspace(.1, 1.0, 20))
    fig.show()
    
if __name__ == "__main__":
    test_learning_curve()	   	
    # test_classification()
