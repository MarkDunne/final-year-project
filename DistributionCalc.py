import csv
import pytz
import itertools
import numpy as np
import random
import TickerList
from datetime import datetime
from zipline.utils.factory import load_bars_from_yahoo

TickerList.tickers = ['AMD', 'CERN', 'COST', 'DELL', 'GPS', 'INTC', 'MMM']

def genWeights(size):
	while True:		
		#create weights so that sum weights = 1
		randomWeights = np.array([[random.choice([0.0, 1.0])] for i in xrange(size)])
		#scaledweights = randomWeights * (1 / np.sum(randomWeights))
		yield randomWeights

if __name__ == '__main__':

	csvFileName = raw_input("CSV File Name: ")

	start = datetime(2010, 1, 1, 0, 0, 0, 0, pytz.utc)
	end   = datetime(2014, 1, 1, 0, 0, 0, 0, pytz.utc)     
	data = load_bars_from_yahoo(stocks=TickerList.tickers, indexes={}, start=start, end=end)

	#use last known price for missing data
	data = data.fillna(method='ffill')

	#fill data at front of series
	data = data.fillna(method='bfill')

	#drop any other data
	data = data.dropna(how='any')

	#now shape of data is finalised
	num_tickers = data.shape[0]
	print 'Number of stocks', num_tickers

	#init csv file
	csvFile = open(csvFileName, 'wb')
	csvWriter = csv.writer(csvFile, delimiter=',')
	csvHeader = np.append(data.keys().values, ['returns', 'sharpe'])
	csvWriter.writerow(csvHeader)

	#create prices matrix
	#shape 		-> m x n, where m = number of stocks, n = sample size
	#prices[0] 	-> price list for first stock
	prices = np.array(map(lambda x: data[x]['price'].values, data.items))

	num_rows = prices.shape[0]
	weightsGenerator = genWeights(num_tickers)

	i = 0
	while True:
		i += 1
		print "testing strategy", i

		weightsVec 		= weightsGenerator.next()
		weightedPrices 	= prices * weightsVec
		weightedSum 	= np.sum(weightedPrices, axis=0)
		normPrices 		= weightedSum / weightedSum[0]
		stddev 			= np.std(normPrices)

		#return
		asset_return 	= normPrices[-1] - 1	

		#sharpe ratio
		risk_free_return = 0
		sharpe = np.sqrt(num_rows) * (asset_return - risk_free_return) / stddev

		#write to csv
		row = np.append(np.squeeze(weightsVec), [asset_return, sharpe])
		csvWriter.writerow(row)

	csvFile.close()