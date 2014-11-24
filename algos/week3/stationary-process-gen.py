import pytz
import numpy as np
from datetime import datetime

from matplotlib import pyplot as plt
from zipline.utils.factory import load_from_yahoo

sample_size = 250

def random_process():
	a = 0
	b = 104
	rho = 0.995
	X, Y = [], []

	aSamples = np.random.normal(size=sample_size)
	bSamples = np.random.normal(size=sample_size)

	for i in range(0, sample_size):
		X.append(i)
		Y.append(a + b)

		a = a * rho + aSamples[i]
		b = b + rho * bSamples[i]

	plt.plot(X, Y)
	plt.show()

def stock_process():
    start = datetime(2010, 1, 1, 0, 0, 0, 0, pytz.utc)
    end = datetime(2011, 1, 1, 0, 0, 0, 0, pytz.utc)
    data = load_from_yahoo(stocks=['AAPL'], indexes={}, start=start, end=end)

    plt.plot(data[:sample_size])
    plt.show()

for i in range(10):
	random_process()