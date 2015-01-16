from scipy import stats
from math import isinf, isnan
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

n225 = pd.DataFrame.from_csv('axjo-1994-2014.csv')#['Adj Close']#.values[::-1]
spy  = pd.DataFrame.from_csv('spy-1994-2014.csv')#['Adj Close']#.values[::-1]
jpyusd = pd.DataFrame.from_csv('CURRFX-JPYUSD.csv')

factor_exchange_rate = False

combined = spy.join(n225, rsuffix='-n225', how='inner').join(jpyusd, how='inner')
#
spy = combined['Adj Close']

if factor_exchange_rate:
    n225 = combined['Adj Close-n225'].mul(combined['Rate'])
else:
    n225 = combined['Adj Close-n225']
#

points = zip(spy.values, n225.values)

plt.plot(spy.values, n225.values, '+', alpha=0.5)
plt.xlabel("SPY value")
plt.ylabel("N225 value")

plt.figure()