import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.neighbors import KNeighborsRegressor
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cross_validation import KFold
from sklearn.cross_validation import cross_val_score
from sklearn.metrics import mean_squared_error
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from plot_learning_curve import plot_learning_curve


def kfold_for_classifier(estimator, X, y, n_folds=10, shuffle=True):
    mses_train = np.zeros(n_folds)
    mses_test = np.zeros(n_folds)
    folds = KFold(n=len(X), n_folds=n_folds, shuffle=shuffle)
    for i, (train_indexes, test_indexes) in enumerate(folds):
        X_train = X[train_indexes]
        y_train = y[train_indexes]
        X_test = X[test_indexes]
        y_test = y[test_indexes]
        estimator.fit(X_train, np.ravel(y_train))
        y_predicted = estimator.predict(X_train)
        mses_train[i] = accuracy_score(y_train, y_predicted)
        y_predicted = estimator.predict(X_test)
        mses_test[i] = accuracy_score(y_test, y_predicted)
    return np.mean(mses_train), np.std(mses_train), np.mean(mses_test), np.std(mses_test)

data_loc = '/home/mark/workspace/final-year-project/data/machines/DJIA-window-history.csv'

print 'loading data'
data = pd.DataFrame.from_csv(data_loc)


print 'reducing data'
sample = np.random.randint(len(data), size=5000)
data = data.ix[sample]

X = data[[0, 1, 2, 3, 4]].values
y = data[['outcome-class']].values

def bias_variance_tradeoff():
    mses_train = np.array([])
    std_train = np.array([])
    mses_test = np.array([])
    std_test = np.array([])

    neighbours = np.arange(1, 60, 2)

    for k in neighbours:
        print 'KNeighborsClassifier(', k, ')'
        estimator = KNeighborsClassifier(k)
        mean_mse_train, std_mse_train, mean_mse_test, std_mse_test = kfold_for_classifier(estimator, X, y, n_folds=8)

        mses_train = np.append(mses_train, mean_mse_train)
        std_train = np.append(std_train, std_mse_train)

        mses_test = np.append(mses_test, mean_mse_test)
        std_test = np.append(std_test, std_mse_test)

    plt.title("Bias-Variance Trade-Off for k-NN Classifier")
    plt.xlabel("Number Neighbours")
    plt.ylabel("Accuracy")

    plt.fill_between(neighbours, mses_train - std_train, mses_train + std_train, alpha=0.1, color="g")
    plt.fill_between(neighbours, mses_test - std_test, mses_test + std_test, alpha=0.1, color="r")

    plt.plot(neighbours, mses_train, 'o-', color="g", label="Training error")
    plt.plot(neighbours, mses_test, 'o-', color="r", label="Cross Validation Error")
    plt.legend(loc="best")
    plt.show()


def test_classifier():
    y = data[['outcome-class']].values.flatten()
    estimator = KNeighborsClassifier(50)
    folds = KFold(n=len(X), n_folds=10, shuffle=True)
    score = cross_val_score(estimator, X, y, cv=folds, scoring='f1')
    print np.mean(score)


def learning_curve():
    estimator = KNeighborsClassifier(50)
    folds = KFold(n=len(X), n_folds=10, shuffle=True)
    fig = plot_learning_curve(estimator, "50-NN learning curve", X, y, cv=folds, verbose=2, train_sizes=np.linspace(.1, 1.0, 25))
    fig.show()

if __name__ == "__main__":
    learning_curve()
