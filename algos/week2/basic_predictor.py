import pytz
from datetime import datetime

from zipline.algorithm import TradingAlgorithm
from zipline.utils.factory import load_from_yahoo
from zipline.finance import commission


STOCKS = ['AMD', 'CERN', 'COST', 'DELL', 'GPS', 'INTC', 'MMM']

class BasicPredicator(TradingAlgorithm):

    def __init__(self, window_start, window_train, window_end):
        super(BasicPredicator, self).__init__()
        self.window_start = window_start
        self.window_train = window_train
        self.window_end   = window_end

    def initialize(self):
        self.stocks = STOCKS
        self.set_commission(commission.PerShare(cost=0))
        print self.all_api_methods

    def handle_data(self, data):      
        pass

if __name__ == '__main__':
    print "starting"
    start = datetime(2010, 1, 1, 0, 0, 0, 0, pytz.utc)
    train = datetime(2013, 1, 1, 0, 0, 0, 0, pytz.utc)
    end   = datetime(2014, 1, 1, 0, 0, 0, 0, pytz.utc)

    #load data and sanitise
    data = load_from_yahoo(stocks=STOCKS, indexes={}, start=start, end=end)
    data = data.dropna()

    #initialise the simulation
    basic_predictor = BasicPredicator(start, train, end)

    #run the simulation
    results = basic_predictor.run(data)