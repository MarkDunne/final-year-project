import pytz
import numpy as np
from datetime import datetime

from collections import deque

from zipline.algorithm import TradingAlgorithm
from zipline.utils.factory import load_from_yahoo
from zipline.finance import commission
from zipline.transforms.ta import *

STOCKS = ['AMD', 'CERN', 'COST', 'DELL', 'GPS', 'INTC', 'MMM']

class BasicPredicator(TradingAlgorithm):

    def __init__(self, window_start, window_train, window_end):
        super(BasicPredicator, self).__init__()
        self.window_start = window_start
        self.window_train = window_train
        self.window_end   = window_end

        self.input_sets = []        
        self.stock_directions = [] 
        self.prediction = []
        
        

    def initialize(self):
        self.stocks = STOCKS    
        self.set_commission(commission.PerShare(cost=0))    
        
        self.days = 0
        self.short_window = 10
        self.long_window = 30
        self.price_history = deque(maxlen = self.long_window)
        
        #Exponential Moving Average
        self.last_ema_test = None
        self.short_ema_trans = EMA(timeperiod = self.short_window)
        self.long_ema_trans  = EMA(timeperiod = self.long_window)
        

    def handle_data(self, data):
        self.days += 1
        if self.days < 50:
            return                
                    
        self.price_history.append(np.array([data[sid]['price'] for sid in data.keys()]))                        
        
        if(len(self.price_history) >= 2):
            self.stock_directions.append(self.price_history[-1] > self.price_history[-2])
        
        self.input_sets.append([
            self.ema_crossover(data),
        ])
                
        print "input", len(self.input_sets)
        print "outcomes", len(self.stock_directions)                
                
        if( self.datetime < self.window_train ):
            self.train(data)
        else:
            self.make_prediction(data)

    def train(self, data):
        pass
    
    def make_prediction(self, data):
        pass
    
    #return 1 if short has crossed over long
    #return 0 if no crossover
    #return -1 if short has crossed under long
    def ema_crossover(self, data):
        short_ema = self.short_ema_trans.handle_data(data)
        long_ema  = self.long_ema_trans.handle_data(data)
                  
        result = np.zeros(short_ema.shape, dtype=np.int)           
        if(np.isnan(short_ema).all() or np.isnan(short_ema).all()):
            return result                                           
                       
        ema_test = short_ema > long_ema
        if self.last_ema_test is not None:          
            result = vchange_direction(last = self.last_ema_test, new = ema_test)          
            
        self.last_ema_test = ema_test
        return result    
        
def change_direction(last, new):
   if last == new:
       return 0
   elif new:
       return 1
   else:
       return -1
       
vchange_direction = np.vectorize(change_direction)
            
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