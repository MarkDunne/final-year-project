import pandas as pd

from sklearn.neighbors import KNeighborsRegressor
from sklearn.grid_search import GridSearchCV
from sklearn.cross_validation import KFold

data_loc = '/home/mark/workspace/final-year-project/data/machines/DJIA-window-history.csv'

data = pd.DataFrame.from_csv(data_loc)
estimator = KNeighborsRegressor()

X = data[[0, 1, 2, 3, 4]].values
y = data[['outcome']].values

hyperparameters = {'n_neighbors' : range(99, 101)}
folds = KFold(n=len(X), n_folds=10, shuffle=True)

gs = GridSearchCV(estimator, hyperparameters, cv = folds, verbose=10)
gs.fit(X, y)

print(gs.best_estimator_)
print(gs.best_score_)
print(gs.best_params_)