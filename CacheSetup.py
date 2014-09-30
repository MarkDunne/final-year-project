import pytz
import TickerList
from datetime import datetime
from zipline.utils.factory import load_bars_from_google

if __name__ == '__main__':
	start = datetime(2013, 1, 1, 0, 0, 0, 0, pytz.utc)
	end   = datetime(2014, 1, 1, 0, 0, 0, 0, pytz.utc)     

	print 'loading stocks'	
	data = load_bars_from_google(stocks=TickerList.tickers, indexes={}, start=start, end=end)