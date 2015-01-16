import numpy as np
import pandas as pd

from pybrain.datasets import SupervisedDataSet
from pybrain.utilities import percentError
from pybrain.structure import FullConnection
from pybrain.structure import FeedForwardNetwork
from pybrain.structure import LinearLayer, SigmoidLayer
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.tools.xml.networkwriter import NetworkWriter
from pybrain.tools.neuralnets import NNregression

window_size = 10
input_size = window_size - 2  # minus 2 because 1 is for target and 1 less because diffs


def windows(data, window_len):
    for i in xrange(0, len(data) - window_len + 1):
        yield [data[j] for j in xrange(i, i + window_len)]


def diff_percent(a):
    return np.true_divide(np.diff(a), a[:-1])

data = pd.io.parsers.read_csv('../../data/spy-1994-2014.csv')['Adj Close'].values

net = FeedForwardNetwork()
inLayer = LinearLayer(input_size)
hiddenLayer1 = SigmoidLayer(20, name="hidden1")
hiddenLayer2 = SigmoidLayer(20, name="hidden2")
outLayer = LinearLayer(1)

net.addInputModule(inLayer)
net.addModule(hiddenLayer1)
net.addModule(hiddenLayer2)
net.addOutputModule(outLayer)

net.addConnection(FullConnection(inLayer, hiddenLayer1))
net.addConnection(FullConnection(hiddenLayer1, hiddenLayer2))
net.addConnection(FullConnection(hiddenLayer1, outLayer))
net.sortModules()

m = 0
dataset = SupervisedDataSet(input_size, 1)
for window in windows(data, window_size):
    window_diffs = diff_percent(window)
    m = min(min(window_diffs), m)
    dataset.addSample(window_diffs[:-1], window_diffs[-1])
print 'max', m

testData, trainData = dataset.splitWithProportion(0.25)

trainer = BackpropTrainer(net, dataset=trainData, momentum=0.1, verbose=True, weightdecay=0.01)

# for i in xrange(20):
#     trainer.trainEpochs(10)

#     trnresult = percentError(trainer.testOnClassData(), trainData)
#     tstresult = percentError(trainer.testOnClassData(dataset=testData), testData)

#     print "epoch: %4d" % trainer.totalepochs, \
#         "train error: %f%%" % trnresult, \
#         "test error: %f%%" % tstresult

#     NetworkWriter.writeToFile(net, "spy-1994-2014-network.xml")
