import urllib
import pandas as pd

auth_token = 'pdRRzNygCjs_YY5Y2MVe'
spy_list_loc = '/home/mark/workspace/final-year-project/data/SP500.csv'


# gather pe data
# symbols = pd.DataFrame.from_csv(spy_list_loc).index.values
# save_loc = '/home/mark/workspace/final-year-project/data/fundamentals/pe-ratios/'
# for symbol in symbols:
#     print 'downloading data for', symbol
#     url = 'https://www.quandl.com/api/v1/datasets/DMDRN/{0}_PE_CURR.csv?collapse=annual&auth_token=pdRRzNygCjs_YY5Y2MVe'.format(symbol)
#     urllib.urlretrieve(url, save_loc + symbol + '.csv')


symbols = pd.DataFrame.from_csv(spy_list_loc).index.values
save_loc = '/home/mark/workspace/final-year-project/data/fundamentals/pe-ratios-delta/'
for symbol in symbols:
    print 'downloading data for', symbol
    url = 'https://www.quandl.com/api/v1/datasets/DMDRN/{0}_PE_CURR.csv?collapse=annual&transformation=rdiff&auth_token=pdRRzNygCjs_YY5Y2MVe'.format(symbol)
    urllib.urlretrieve(url, save_loc + symbol + '.csv')


## gather annual return data
#symbols = pd.DataFrame.from_csv(spy_list_loc)
#save_loc = '/home/mark/workspace/final-year-project/data/fundamentals/annual-returns/'
#for symbol in symbols.iterrows():
#    print 'downloading data for', symbol[0]
#    url = 'https://www.quandl.com/api/v1/datasets/{0}.csv?transformation=rdiff&collapse=annual&auth_token=pdRRzNygCjs_YY5Y2MVe'.format(symbol[1]['Code'])
#    urllib.urlretrieve(url, save_loc + symbol[0] + '.csv')
