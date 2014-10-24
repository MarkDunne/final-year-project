import pytz
import talib
import numpy as np
from collections import defaultdict
from sklearn import tree
from datetime import datetime
from sklearn.metrics import confusion_matrix
from sklearn.neighbors import KNeighborsClassifier
from scipy.stats import itemfreq
from collections import Counter

# Put any initialization logic here.  The context object will be passed to
# the other methods in your algorithm.
def initialize(context):
    context.days = 0
    context.prediction_count = 0

    #context.stocks = symbols('AMD', 'CERN', 'COST', 'DELL', 'GPS', 'INTC', 'MMM')
    context.stocks = symbols('AXP', 'BA', 'CAT', 'CSCO', 'CVX', 'DD', 'DIS', 'GE', 'GS', 'HD', 'IBM', 'INTC', 'JNJ', 'JPM', 'KO', 'MCD', 'MMM', 'MRK', 'MSFT', 'NKE', 'PFE', 'PG', 'UNH', 'UTX', 'VZ', 'WMT', 'XOM')
    #context.stocks = [sid(8554), sid(2174), sid(19920), sid(41710), sid(22090)];

        
    #windows
    context.short_window = 5
    context.long_window = 10
    context.training_window = 300

    #The last comparison of Moving Averages
    context.last_ma_tests = dict()

    context.inputs = []
    context.outcomes = []
    context.machine = KNeighborsClassifier(n_neighbors=3)
    context.predicted_outcomes = defaultdict(lambda: None)
    context.prediction_history = []

    context.y_pred = []
    context.y_true = []

    context.count_equal = 0.0
    context.count_gt = 0.0
    context.count_lt = 0.0

# Will be called on every trade event for the securities you specify. 
def handle_data(context, data):
    context.days += 1
    if context.days < context.long_window:
        return                      
        
    price_history = history(100, '1d', 'price').ffill().bfill()
    high_history  = history(100, '1d', 'high').ffill().bfill()
    low_history   = history(100, '1d', 'low').ffill().bfill()
    close_history = history(100, '1d', 'close_price').ffill().bfill()  

    analysis_vectors = np.transpose([
        ma_crossover(context, data),
        stoch(context, data, high_history, low_history, close_history),
        bbands_crossover(context, data, price_history),
        atr_breakout(context, data, high_history, low_history, close_history),
        macd(context, data, price_history),
    ])    


    outcomes_vector = dict()
    for sid in context.stocks:
        yest_price = price_history[sid][-2]
        today_price = price_history[sid][-1]

        if today_price - 0.01 > yest_price:
            outcomes_vector[sid] = "gt"
        elif today_price + 0.01 < yest_price:
            outcomes_vector[sid] = "lt"
        else:
            outcomes_vector[sid] = "eq"  
            context.count_equal += 1
            
    #record(eq=context.count_equal)

    context.inputs.extend(analysis_vectors)
    context.outcomes.extend(outcomes_vector.values())
        
    #training
    if context.days % context.training_window == 0:
        #shave first set of outcomes and last set of inputs
        n = len(context.stocks)
        context.inputs = context.inputs[:-n]
        context.outcomes = context.outcomes[n:]
        
        log.info( 'fitting machine' )
        context.machine.fit(context.inputs, context.outcomes)
        log.info( 'finished fitting machine' )

    #predicting
    if context.days > context.training_window:               
        #compare last predictions
        for sid, prediction in context.predicted_outcomes.iteritems():
            if prediction is not None:
                context.y_pred.append(prediction)
                context.y_true.append(outcomes_vector[sid]) 
        #make next prediction
        for i, input_vector in enumerate(analysis_vectors):   
            sid = context.stocks[i]
            next_prediction = context.machine.predict(input_vector)[0]
            context.predicted_outcomes[sid] = next_prediction

        if context.days % 100 == 0:
            cm = confusion_matrix(context.y_true, context.y_pred, labels=["gt", "lt", "eq"])
            log.info(cm)
            log.info(prediction_rate(cm))           

def prediction_rate(cm):
    total = np.sum(cm)
    if total == 0:
        return 0

    correct_pred_total = 0.0
    for i, row in enumerate(cm):
        correct_pred_total += row[i]

    return correct_pred_total / total
            
def short_mavg(data, sid):
    return data[sid].vwap(5)

def long_mavg(data, sid):
    return data[sid].vwap(10)             
    
#return array of ma crossover test results   
def ma_crossover(context, data):
    cross_direction = []
    for stock in context.stocks:
        
        short_ma = short_mavg(data, stock)
        long_ma = long_mavg(data, stock)
        ma_test = short_ma > long_ma
        
        if stock in context.last_ma_tests:
            if context.last_ma_tests[stock] == ma_test:
                cross_direction.append(0)
            elif ma_test:
                cross_direction.append(1)
            else:
                cross_direction.append(-1)
        else:
            cross_direction.append(0)
            
        context.last_ma_tests[stock] = ma_test
    
    return cross_direction

def bbands_crossover(context, data, price_history):
    cross_direction = []
    for stock in context.stocks:
        price = data[stock].price
     
        if np.isnan(price_history[stock]).all():
            cross_direction.append(0)
            continue

        #calculate bbands
        upper, middle, lower = talib.BBANDS(
            price_history[stock],
            timeperiod = context.short_window,
            nbdevup = 3.5,
            nbdevdn = 3.5,
            matype = 0 )
        
        if price <= lower[-1]:
            cross_direction.append(-1)
        elif price >= upper[-1]:
            cross_direction.append(1)
        else:
            cross_direction.append(0)
    
    return cross_direction

def atr_breakout(context, data, high_history, low_history, close_history):
    cross_direction = []
    for stock in context.stocks:
        price = data[stock].price
     
        if np.isnan(high_history[stock]).all():
            cross_direction.append(0)
            continue

        #calculate atr
        atr = talib.ATR(
            high_history[stock],
            low_history[stock],
            close_history[stock],
            timeperiod = context.short_window)[-1]
        
        prev_close = close_history.iloc[-3][stock]
        up_signal = price - (prev_close + atr)
        dn_signal = prev_close - (price + atr)
        
        if up_signal > 0:
            cross_direction.append(1)
        elif dn_signal > 0:
            cross_direction.append(-1)
        else:
            cross_direction.append(0)
    
    return cross_direction

def macd(context, data, price_history):
    cross_direction = []
    for stock in context.stocks:
 
        if np.isnan(price_history[stock]).all():
            cross_direction.append(0)
            continue

        #calculate atr
        macd, signal, hist = talib.MACD(
                price_history[stock],
                fastperiod = context.short_window,
                slowperiod = context.long_window,
                signalperiod = 7)
        
        val = macd[-1] - signal[-1]
        
        if val > 0.5:
            cross_direction.append(1)
        elif val < -0.5:
            cross_direction.append(-1)
        else:
            cross_direction.append(0)
    
    return cross_direction

def stoch(context, data, high_history, low_history, close_history):
    cross_direction = []
    for stock in context.stocks:
    
        if np.isnan(high_history[stock]).all():
            cross_direction.append(0)
            continue

        slowk, slowd = talib.STOCH(high_history[stock],
                               low_history[stock],
                               close_history[stock],
                               fastk_period=5,
                               slowk_period=3,
                               slowk_matype=0,
                               slowd_period=3,
                               slowd_matype=0)
        
        slowk = slowk[-1]
        slowd = slowd[-1]
        
        if slowk < 10 or slowd < 10:
            cross_direction.append(1)
        elif slowk > 90 or slowd > 90:
            cross_direction.append(-1)
        else:
            cross_direction.append(0)
    
    return cross_direction    

            