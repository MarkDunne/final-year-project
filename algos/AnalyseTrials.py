import numpy as np
import pandas as pd

data = pd.read_csv("olmar-strategy-test_2.csv")
data = data.dropna()
data = data['returns'].values

mean = np.mean(data)
stdev = np.std(data)

print mean, stdev