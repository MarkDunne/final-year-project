import numpy as np
import pandas as pd

data = np.array(pd.read_csv("olmar.csv")['portfolio_value'])
norm = data / data[0]

stddev = np.std(norm)
asset_return = norm[-1] - 1

risk_free_return = 0
sharpe = (asset_return - risk_free_return) / stddev

print asset_return, sharpe