import csv
import pandas as pd

spy_list_loc = '/home/mark/workspace/final-year-project/data/SP500.csv'
returns_loc = '/home/mark/workspace/final-year-project/data/fundamentals/annual-returns/'
ratios_loc = '/home/mark/workspace/final-year-project/data/fundamentals/pe-ratios-delta/'

save_loc = '/home/mark/workspace/final-year-project/data/fundamentals/pe_delta_returns.csv'

symbols = pd.DataFrame.from_csv(spy_list_loc).index.values

pe_returns = []
successful_parses = 0

for symbol in symbols:
    symbol_parsed = False
    ratios = pd.DataFrame.from_csv(ratios_loc + symbol + '.csv')
    returns = pd.DataFrame.from_csv(returns_loc + symbol + '.csv')

    years = [str(year) + '1231' for year in range(1990, 2015)]

    for i, year in enumerate(years[:-1]):
        try:
            pe_returns.append([symbol, ratios[years[i]]['Current PE Ratio'].values[0], returns[years[i+1]]['Close'].values[0]])
            symbol_parsed = True
        except Exception, e:
            pass

    if not symbol_parsed:
        print symbol
    else:
        successful_parses += 1
        print 'successful parses', successful_parses

with open(save_loc, "wb") as f:
    writer = csv.writer(f)
    writer.writerow(['symbol', 'pe-delta-ratio', 'returns'])
    writer.writerows(pe_returns)
