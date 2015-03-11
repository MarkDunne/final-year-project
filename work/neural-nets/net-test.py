import numpy as np
import pandas as pd
from pybrain.tools.xml.networkreader import NetworkReader

window_size = 10
# minus 2 because 1 is for target and 1 less because diffs
input_size = window_size - 2


def windows(data, window_len):
    for i in xrange(0, len(data) - window_len + 1):
        yield [data[j] for j in xrange(i, i + window_len)]


def diff_percent(a):
    return np.true_divide(np.diff(a), a[:-1])

data = pd.io.parsers.read_csv(
    '../../data/spy-1994-2014.csv')['Adj Close'].values
net = NetworkReader.readFrom(
    '/home/mark/workspace/final-year-project/work/neural-nets/spy-1994-2014-network.xml')

for window in windows(data, window_size):
    dp = diff_percent(window)
    window_inputs = dp[:-1]
    window_target = dp[-1]
    net_result = net.activate(window_inputs)
    print net_result
