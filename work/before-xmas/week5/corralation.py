from scipy import stats
from math import isinf, isnan
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

n225 = pd.DataFrame.from_csv('n225-1994-2014.csv')#['Adj Close']#.values[::-1]
spy  = pd.DataFrame.from_csv('spy-1994-2014.csv')#['Adj Close']#.values[::-1]

#print spy.corr(n225)
#
combined = spy.join(n225, rsuffix='-n225', how='inner')
#
spy = (combined['Adj Close'])
n225 = (combined['Adj Close-n225'])
#
#for i in range(len(spy)):
#    plt.plot(spy[i], n225[i], '+')
#
#plt.show()
#print np.corrcoef(spy, n225)

def normalize(ns):
    def calc(a, b):
        ans = (a - b) / b
        if isinf(ans) or isnan(ans):
            return a
        return ans
        
    return [calc(a,b) for (a,b) in zip(ns[1:], ns) ]

spy_deltas = normalize(np.diff(spy))
n225_deltas = normalize(np.diff(n225))

print np.corrcoef(spy_deltas, n225_deltas)