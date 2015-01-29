import numpy as np
import pandas as pd
from scipy import stats
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

def to_percent(y, position):
    # Ignore the passed in position. This has the effect of scaling the default
    # tick locations.
    s = str(100 * y)

    # The percent symbol needs escaping in latex
    if matplotlib.rcParams['text.usetex'] == True:
        return s + r'$\%$'
    else:
        return s + '%'

pe_returns = '../../data/fundamentals/pe_delta_returns.csv'

data = pd.DataFrame.from_csv(pe_returns)
data = data[(np.abs(stats.zscore(data)) < 1).all(axis=1)]

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

plt.ylabel(r'\textit{P/E Ratio Change Year Previous}')
plt.xlabel(r'\textit{Stock Price Change Year Following}')

xticks = mticker.FuncFormatter(to_percent)
plt.gca().xaxis.set_major_formatter(xticks)

points = data.values
xs = data['returns']
ys = data['pe-delta-ratio']

fit = np.polyfit(xs, ys, 1)
fit_fn = np.poly1d(fit)

low_pe_ratio = data[stats.zscore(data['pe-delta-ratio']) <= 1]
high_pe_ratio = data[stats.zscore(data['pe-delta-ratio']) > 1]

xs = low_pe_ratio['returns']
ys = low_pe_ratio['pe-delta-ratio']
low_pe_mean = xs.mean()
plt.plot(xs, ys, 'r.', xs, fit_fn(xs), 'k')
plt.axvline(xs.mean(), color='r', linestyle='dashed', linewidth=2)

plt.text(10.1,0,'blah',rotation=90)

xs = high_pe_ratio['returns']
ys = high_pe_ratio['pe-delta-ratio']
high_pe_mean = xs.mean()
plt.plot(xs, ys, 'b.', xs, fit_fn(xs), 'k')
plt.axvline(xs.mean(), color='b', linestyle='dashed', linewidth=2)

plt.savefig('delta_pe_ratio_returns_clean')
plt.show()

test = stats.ttest_ind(high_pe_ratio['returns'].values, low_pe_ratio['returns'].values)

print test
print 'mean difference'
print high_pe_ratio.mean() - low_pe_ratio.mean()