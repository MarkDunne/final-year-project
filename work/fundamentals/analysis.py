import numpy as np
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

pe_returns = '/home/mark/workspace/final-year-project/data/fundamentals/pe_delta_returns.csv'

data = pd.DataFrame.from_csv(pe_returns)
data = data[(np.abs(stats.zscore(data)) < 1).all(axis=1)]

plt.xlabel('pe ratio % change year previous')
plt.ylabel('stock price % change year following')

points = data.values
xs = points[: , 0]
ys = points[: , 1]

fit = np.polyfit(xs, ys, 1)
fit_fn = np.poly1d(fit)

plt.plot(xs, ys, 'r.', xs, fit_fn(xs), 'k')
plt.show()

low_pe_ratio = data[stats.zscore(data['pe-delta-ratio']) <= 1]
high_pe_ratio = data[stats.zscore(data['pe-delta-ratio']) > 1]

test = stats.ttest_ind(low_pe_ratio['returns'].values, high_pe_ratio['returns'].values)

print test
print 'mean difference'
print high_pe_ratio.mean() - low_pe_ratio.mean()