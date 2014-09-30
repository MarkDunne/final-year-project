import pytz
import itertools
import TickerList
import numpy as np
from datetime import datetime
from zipline.utils.factory import load_bars_from_google

def sharpe(prices):

	normPrices = prices / prices[0]
	stddev = np.std(normPrices)

	if stddev == 0 or normPrices[0] == 0:
		return np.nan

	n = len(normPrices)
	risk_free_return = 0
	asset_return = normPrices[-1] - 1	


	return (asset_return - risk_free_return) / stddev

if __name__ == '__main__':
	start = datetime(2013, 1, 1, 0, 0, 0, 0, pytz.utc)
	end   = datetime(2014, 1, 1, 0, 0, 0, 0, pytz.utc)     

	data = load_bars_from_google(stocks=['AAPL', 'GOOG', 'MSFT'], indexes={}, start=start, end=end)

	#create prices matrix
	#shape 		-> m x n, where m = number of stocks, n = sample size
	#prices[0] 	-> price list for first stock
	prices = np.array(map(lambda x: data[x]['price'].values, data.items))

	for weightsVec in itertools.product([[0], [1]], repeat=3):
		#multiply prices by a 1d weights array (actually a trivial 2d array)
		#see http://stackoverflow.com/questions/24253021/numpy-multiplying-a-2d-array-by-a-1d-array
		#weighted prices * np.array([[1], [0], [1]])

		weightedPrices = prices * weightsVec
		weightedSum = np.sum(weightedPrices, axis=0)
		print sharpe(weightedSum)