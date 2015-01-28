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

pe_returns = '/home/mark/workspace/final-year-project/data/fundamentals/pe_absolute_returns.csv'

data = pd.DataFrame.from_csv(pe_returns)
data = data[(np.abs(stats.zscore(data)) < 1).all(axis=1)]

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

plt.ylabel(r'\textit{P/E Ratio Year Previous}')
plt.xlabel(r'\textit{Stock Price Change Year Following}')

xticks = mticker.FuncFormatter(to_percent)
plt.gca().xaxis.set_major_formatter(xticks)

points = data.values
ys = points[: , 0]
xs = points[: , 1]

fit = np.polyfit(xs, ys, 1)
fit_fn = np.poly1d(fit)

plt.plot(xs, ys, 'r.', xs, fit_fn(xs), 'k')
#plt.savefig('absolute_pe_ratio_returns_unclean')
plt.show()

low_pe_ratio = data[stats.zscore(data['pe-absolute-ratio']) <= 1]
high_pe_ratio = data[stats.zscore(data['pe-absolute-ratio']) > 1]

test = stats.ttest_ind(low_pe_ratio['returns'].values, high_pe_ratio['returns'].values)

print test
print 'mean difference'
print high_pe_ratio.mean() - low_pe_ratio.mean()