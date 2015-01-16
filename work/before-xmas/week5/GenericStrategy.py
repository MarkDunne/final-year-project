from pyalgotrade import strategy
from pyalgotrade.barfeed import yahoofeed

import numpy as np
from sklearn.metrics import confusion_matrix

class GenericStrategy(strategy.BacktestingStrategy):
    def __init__(self, instruments, window_size, analyse_freq=10):
        strategy.BacktestingStrategy.__init__(self, self.getFeed(instruments))
        self.bar_counter = 0
        self.instruments = instruments
        
        self.window_size = window_size
        self.history_available = False
        self.history_count = 0
        self.pred_history_count = 0
        self.history = dict([(instrument, []) for instrument in self.instruments])
        self.pred_history =  dict([(instrument, []) for instrument in self.instruments])
        self.direction_history = dict([(instrument, []) for instrument in self.instruments])            
        self.analyse_freq = analyse_freq

    def inst_history(self, instrument):
        return np.array(self.history[instrument])

    def inst_history_window(self, instrument):
        return np.array(self.history[instrument][-self.window_size])

    def onBars(self, bars):
        if self.bar_counter >= self.window_size:
            self.history_available = True
            
            #prediction rate so far
            if self.bar_counter % self.analyse_freq == 0:
                if self.history_count - 1 != self.pred_history_count:
                    print 'actual and prediction count mismatch'
                    print 'len history', len(self.history_count), 'len predictions', len(self.pred_history_count)
                else:
                    y_true = []
                    y_pred = []
                    for pred, actual in zip(self.pred_history.items, self.history[1:].items):
                        for instrument in self.instruments:
                            y_true.append(actual[instrument])
                            y_pred.append(pred[instrument])
                    
                    cm = confusion_matrix(y_true, y_pred, labels=[1, -1, 0])
                    self.log_conf_matrix(cm)
        
            #call child
            self.bar_predictions = dict()
            self.handle_onBars(bars)     

        #update history    
        self.bar_counter += 1
        for instrument in self.instruments:
            if self.history_count > 0:            
                last_direction = self.discretize_price_diff(bars[instrument].getClose(), self.history[instrument][-1])
                self.direction_history[instrument].append(last_direction)
            self.history[instrument].append(bars[instrument].getClose())
            self.history_count += 1
        
    def handle_onBars(self, bars):
        pass

    def discretize_price_diff(self, p1, p2, range=0):
        if p1 - range > p2:
            return 1
        elif p1 + range < p2:
            return -1
        else:
            return 0
          
    def make_predictions(self, predictions):
        self.pred_history_count += 1
        for instrument in self.instruments:
            if instrument not in predictions:
                print 'error - must have predictions for all instruments - missing for ' + instrument
            else:
                self.pred_history[instrument].append(predictions[instrument])
        
          
    def log_conf_matrix(self, cm):
        total = np.sum(cm)
        if total == 0:
            return 0
    
        correct_pred_total = 0.0
        for i, row in enumerate(cm):
            correct_pred_total += row[i]
    
        self.info(cm)
        self.info(correct_pred_total / total)

    def getFeed(self, instruments):    
        #TODO
        #load from [yahoo|google|quandl] if not available
        #check for stock splits
        #add date ranges
        feed = yahoofeed.Feed()
        for instrument in instruments:
            feed.addBarsFromCSV(instrument, instrument + "-2010.csv") 
        return feed   
