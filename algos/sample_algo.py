def initialize(context):

    context.aapl = sid(24)


class VWAP(TradingAlgorithm):
	def initialize(self):
		self.trading_days = 0

	def handle_data(context, data):

		if trading_days:
			pass

	    vwap = data[context.aapl].vwap(3)
	    price = data[context.aapl].price
	    
	    if price < vwap * 0.995:
	        order(context.aapl,-100)

	    elif price > vwap * 1.005:
	        order(context.aapl,+100)

if __name__ == '__main__':
    import pylab as pl
    start = datetime(2010, 1, 1, 0, 0, 0, 0, pytz.utc)
    end = datetime(2014, 1, 1, 0, 0, 0, 0, pytz.utc)
    data = load_from_yahoo(stocks=STOCKS, indexes={}, start=start,
                           end=end)
    data = data.dropna()
    olmar = OLMAR()
    results = olmar.run(data)
    results.portfolio_value.plot()
    results.portfolio_value.to_csv("olmar.csv", header=True)
    pl.show()