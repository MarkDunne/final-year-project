import pytz
import numpy as np
from datetime import datetime
from zipline.algorithm import TradingAlgorithm
from zipline.utils.factory import load_from_yahoo
from zipline.api import order_target, record, symbol, history, add_history

STOCKS = ['AMD', 'CERN', 'COST', 'DELL', 'GPS', 'INTC', 'MMM']

class BasicPredicator(TradingAlgorithm):
    def initialize(context):
        # Register 2 histories that track daily prices,
        # one with a 100 window and one with a 300 day window
        self.add_history(100, '1m', 'price')
        self.add_history(300, '1m', 'price')

        context.i = 0


    def handle_data(context, data):
        # Skip first 300 days to get full windows
        context.i += 1
        if context.i < 300:
            return

        # Compute averages
        # history() has to be called with the same params
        # from above and returns a pandas dataframe.
        short_mavg = self.history(100, '1m', 'price').mean()
        long_mavg = self.history(300, '1m', 'price').mean()

        sym = symbol('AAPL')

        # Trading logic
        if short_mavg[sym] > long_mavg[sym]:
            # order_target orders as many shares as needed to
            # achieve the desired number of shares.
            order_target(sym, 100)
        elif short_mavg[sym] < long_mavg[sym]:
            order_target(sym, 0)

        # Save values for later inspection
        record(AAPL=data[sym].price,
               short_mavg=short_mavg[sym],
               long_mavg=long_mavg[sym])

if __name__ == '__main__':
    print "starting"
    start = datetime(2010, 1, 1, 0, 0, 0, 0, pytz.utc)
    train = datetime(2013, 1, 1, 0, 0, 0, 0, pytz.utc)
    end   = datetime(2014, 1, 1, 0, 0, 0, 0, pytz.utc)

    #load data and sanitise
    data = load_from_yahoo(stocks=STOCKS, indexes={}, start=start, end=end)
    data = data.dropna()

    #initialise the simulation
    basic_predictor = BasicPredicator()

    #run the simulation
    results = basic_predictor.run(data)