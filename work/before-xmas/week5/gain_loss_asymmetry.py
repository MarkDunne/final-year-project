import pandas as pd
import numpy as np
import pylab as P
from scipy.stats import norm
import matplotlib.mlab as mlab


def random_process():
    a = 0
    b = 104
    rho = 0.995
    Y = []

    aSamples = np.random.normal(size=3500)
    bSamples = np.random.normal(size=3500)

    for i in range(0, 3500):
        Y.append(a + b)

        a = a * rho + aSamples[i]
        b = b + rho * bSamples[i]

    return Y


def best_number_of_bins(data, minbins=8, maxbins=256):
    """ best_number_of_bins(minbins=8, maxbins=256)

    Calculates the best number of bins to make a histogram 
    of this data, according to Freedman-Diaconis rule.

    """
    q75, q25 = np.percentile(data, [75, 25])
    iqr = q75 - q25
    drange = max(data) - min(data)

    # Get number of bins according to Freedman-Diaconis rule
    bin_size = 2 * iqr * len(data)**(-1.0 / 3)
    nbins = drange / (bin_size + 0.001)
    nbins = max(minbins, min(maxbins, int(nbins)))

    # Done
    return nbins

spy = pd.read_csv(
    '../../../data/dow-2000-2014.csv')['Adjusted Close'].values[::-1]
#spy = random_process()
n = len(spy)

gains = []
loses = []

for i in range(n):
    a = spy[i]
    for j in range(i + 1, n):
        d = (spy[j] - a) / a
        if d <= -0.05:
            loses.append(j - i)
            break
        elif d >= 0.05:
            gains.append(j - i)
            break


n, bins, patches = P.hist(gains, best_number_of_bins(gains), normed=1)
P.setp(patches, 'facecolor', 'g', 'alpha', 0.5)

(mu, sigma) = norm.fit(gains)
y = mlab.normpdf(bins, mu, sigma)
l = P.plot(bins, y, 'g--', linewidth=2, label='Days to gain 5% value')


n, bins, patches = P.hist(
    loses, best_number_of_bins(loses), normed=1, histtype='stepfilled')
P.setp(patches, 'facecolor', 'r', 'alpha', 0.5)

(mu, sigma) = norm.fit(loses)
y = mlab.normpdf(bins, mu, sigma)
l = P.plot(bins, y, 'r--', linewidth=2, label='Days to lose 5% value')

ax = P.gca()
ax.set_ylim(bottom=None, top=0.04)

P.xlabel("Days")
P.ylabel("Frequency")
P.title('Gain/Loss Asymmetry on the Dow Jones')
P.legend()

P.figure()
P.show()

print(np.average(gains))
print(np.average(loses))

print(len(gains))
print(len(loses))
