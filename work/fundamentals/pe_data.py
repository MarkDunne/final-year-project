import pandas as pd
import Quandl

auth_token = 'pdRRzNygCjs_YY5Y2MVe'
spy_list_loc = '/home/mark/workspace/final-year-project/data/SP500.csv'


# gather pe data
# symbols = pd.DataFrame.from_csv(spy_list_loc).index.values
# save_loc = '/home/mark/workspace/final-year-project/data/fundamentals/pe-ratios/'
# for symbol in symbols:
#     print 'downloading data for', symbol
#     url = 'https://www.quandl.com/api/v1/datasets/DMDRN/{0}_PE_CURR.csv?collapse=annual&auth_token=pdRRzNygCjs_YY5Y2MVe'.format(symbol)
#     urllib.urlretrieve(url, save_loc + symbol + '.csv')


# symbols = pd.DataFrame.from_csv(spy_list_loc).index.values
# save_loc = '/home/mark/workspace/final-year-project/data/fundamentals/pe-ratios-delta/'
# for symbol in symbols:
#    print 'downloading data for', symbol
#    url = 'https://www.quandl.com/api/v1/datasets/DMDRN/{0}_PE_CURR.csv?collapse=annual&transformation=rdiff&auth_token=pdRRzNygCjs_YY5Y2MVe'.format(symbol)
#    urllib.urlretrieve(url, save_loc + symbol + '.csv')
#

# gather annual return data
symbols = pd.DataFrame.from_csv(spy_list_loc)

# save_loc = '/home/mark/workspace/final-year-project/data/fundamentals/annual-returns/'
# for symbol in symbols.index:
#     try:
#         print 'downloading data for', symbol

#         query = 'WIKI/' + symbol
# data = Quandl.get(query, collapse='annual', transformation='rdiff',
# authtoken=auth_token)['Adj. Close']

#         data.to_csv(save_loc + symbol + '.csv')
#     except Exception, e:
#         pass

symbols = pd.DataFrame.from_csv(spy_list_loc)
save_loc = '/home/mark/workspace/final-year-project/data/fundamentals/pb-ratios-abs/'
for i, symbol in enumerate(symbols.index):
	print 'downloading data for', symbol, i, '/', len(symbols)
	try:
		query='DMDRN/' + symbol + '_P_BV'
		book_values = Quandl.get(query, authtoken=auth_token)
		book_values.to_csv(save_loc + symbol + '.csv')
	except Exception, e:
		pass
