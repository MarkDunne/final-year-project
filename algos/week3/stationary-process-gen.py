import numpy as np
from datetime import datetime
import pytz

from zipline.utils.factory import load_from_yahoo

from random import random
from matplotlib import pyplot as plt


def random_process():
	y_t = 0
	err = 5
	rho = 0.995

	X = []
	Y = []

	for i in range(0, 250):
		X.append(i)
		Y.append(y_t)
		y_t = y_t * rho + err * (0.5 - random())

	plt.plot(X, Y)

	plt.show()

def stock_process():
    start = datetime(2010, 1, 1, 0, 0, 0, 0, pytz.utc)
    end = datetime(2011, 1, 1, 0, 0, 0, 0, pytz.utc)
    data = load_from_yahoo(stocks=['SPY'], indexes={}, start=start, end=end)

    plt.plot(data)
    plt.show()

random_process()