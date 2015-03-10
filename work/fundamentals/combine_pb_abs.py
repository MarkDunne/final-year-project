import csv
import math
import pandas as pd
from datetime import datetime

spy_list_loc = '/home/mark/workspace/final-year-project/data/SP500.csv'
returns_loc = '/home/mark/workspace/final-year-project/data/fundamentals/annual-returns/'
ratios_loc = '/home/mark/workspace/final-year-project/data/fundamentals/pb-ratios-abs/'

save_loc = '/home/mark/workspace/final-year-project/data/fundamentals/pb_abs_returns.csv'

symbols = pd.DataFrame.from_csv(spy_list_loc).index.values

pb_returns = []
successful_parses = 0

for symbol in symbols:
    symbol_parsed = False

    try:
        years = [datetime(x, 12, 31) for x in range(2000, 2014)]
        ratios = pd.DataFrame.from_csv(ratios_loc + symbol + '.csv')
        returns = pd.DataFrame.from_csv(returns_loc + symbol + '.csv', header=None)
    except Exception, e:
        continue

    for i in range(len(years)):
        try:
            pb = ratios.ix[years[i]]['Price to Book Value Ratio']
            year_returns = returns.ix[years[i + 1]].values[0]
            if not (math.isnan(pb) or math.isnan(year_returns)):
                pb_returns.append([symbol, pb, year_returns])
            symbol_parsed = True
        except Exception, e:
            pass

    if not symbol_parsed:
        pass
    else:
        successful_parses += 1
        print 'successful parses', successful_parses

with open(save_loc, "wb") as f:
    writer = csv.writer(f)
    writer.writerow(['symbol', 'pb-abs-ratio', 'returns'])
    writer.writerows(pb_returns)
