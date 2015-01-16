from pyalgotrade import strategy
from pyalgotrade.barfeed import yahoofeed
from collections import deque

import numpy as np
import statsmodels.tsa.ar_model as ar_mod
from sklearn.metrics import confusion_matrix

class MyStrategy(strategy.BacktestingStrategy):
    def __init__(self, feed, instrument):
        strategy.BacktestingStrategy.__init__(self, feed)
        self.instrument = instrument
        self.history_size = 100
        self.history = deque(maxlen=self.history_size)
        self.bar_counter = 0
        self.prediction_history = []
        self.actual_history = []

    def inst_history(self, instrument):
        return np.array([bars[instrument].getClose() for bars in self.history])

    def onBars(self, bars):
        if self.bar_counter >= self.history_size:

            price = bars[self.instrument].getClose();
            history = self.inst_history(self.instrument)

            offset = self.history_size            
            ar_res = ar_mod.AR(history).fit()
            prediction = ar_res.predict(start=offset, end=offset, dynamic=True)[0]
            
            predicted_price_category = self.discretize_price_diff(prediction, price)
            last_actual_price_category = self.discretize_price_diff(price, history[-1])

            self.prediction_history.append(predicted_price_category)
            self.actual_history.append(last_actual_price_category)

            if self.bar_counter % 10 == 0:
                y_pred  = self.prediction_history[:-1]
                y_true = self.actual_history[1:]
                self.print_cm(confusion_matrix(y_true, y_pred, labels=[1, -1, 0]))

        self.bar_counter += 1
        self.history.append(bars)
    
    def discretize_price_diff(self, p1, p2):
        if p1 - 0.3 > p2:
            return 1
        elif p1 + 0.3 < p2:
            return -1
        else:
            return 0
            
    def print_cm(self, cm):
        total = np.sum(cm)
        if total == 0:
            return 0
    
        correct_pred_total = 0.0
        for i, row in enumerate(cm):
            correct_pred_total += row[i]    

        self.info("\n" + str(cm))
        self.info("accuracy: " + str(correct_pred_total / total))
        self.info("condition counts: " + str(np.sum(cm, axis=0)))
        self.info("condition prcnts: " + str(100.0 * np.sum(cm, axis=0) / total))

feed = yahoofeed.Feed()
feed.addBarsFromCSV("spy", "spy-2010.csv")

# Evaluate the strategy with the feed's bars.
myStrategy = MyStrategy(feed, "spy")
myStrategy.run()