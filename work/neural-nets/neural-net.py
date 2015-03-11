import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.tools.shortcuts import buildNetwork

data_loc = '/home/mark/workspace/final-year-project/data/machines/DJIA-window-history-small.csv'

print 'loading data'
data = pd.DataFrame.from_csv(data_loc)

print 'reducing data'
sample = np.random.randint(len(data), size=5000)
data = data.ix[sample]

X = data[[0, 1, 2, 3, 4]].values
y = data[['outcome']].values

print 'building net'
net = buildNetwork(5, 20, 1, recurrent=False)

dataset = SupervisedDataSet(5, 1)
dataset.setField('input', X)
dataset.setField('target', y)

trainset, testset = dataset.splitWithProportion(0.75)
trainer = BackpropTrainer(net, dataset=trainset, learningrate=0.1, momentum=0.5, verbose=False)

epochs = np.array([])
train_errors = np.array([])
test_errors = np.array([])

for i in range(10):
    print 'round', i + 1
    trainer.trainEpochs(5)

    train_error = trainer.testOnData(trainset)
    test_error = trainer.testOnData(testset)

    epochs = np.append(epochs, trainer.totalepochs)
    train_errors = np.append(train_errors, train_error)
    test_errors = np.append(test_errors, test_error)

    print 'train error', train_error
    print 'test error', test_error


plt.title("Learning rate for 5-20-1 Neural Net")
plt.xlabel("Epoch")
plt.ylabel("MSE")
plt.plot(epochs, train_errors, 'o-', color="g", label="Training error")
plt.plot(epochs, test_errors, 'o-', color="r", label="Testing error")
plt.legend(loc="best")
plt.show()
