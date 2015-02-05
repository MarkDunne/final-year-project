import numpy as np
import pandas as pd
import Quandl

auth = 'pdRRzNygCjs_YY5Y2MVe'
dow_list = '/home/mark/workspace/final-year-project/data/dowjonesIA.csv'
save_loc = '/home/mark/workspace/final-year-project/data/machines/DJIA-window-history.csv'

def windows(data, window_len):
    for i in xrange(0, len(data) - window_len + 1):
        yield [data[j] for j in xrange(i, i + window_len)]

dowjonesIA = pd.DataFrame.from_csv(dow_list)
output = pd.DataFrame()

for ticker, row in dowjonesIA.iterrows():
    print 'Processing', row['Name']
    data = Quandl.get(row['Code'], transformation='rdiff', authtoken=auth)
    close_prices = data['Close']

    for window in windows(data=close_prices, window_len=6):
        row = pd.Series(np.concatenate([window, [window[-1] > 0]]))
        if not np.isnan(row).any():
            output = output.append(row, ignore_index=True)

output.columns = [0, 1, 2, 3, 4, 'outcome', 'outcome-class']
output.to_csv(save_loc)