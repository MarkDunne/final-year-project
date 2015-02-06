import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

data_loc = '/home/mark/workspace/final-year-project/data/machines/DJIA-window-history.csv'

print 'loading data'
data = pd.DataFrame.from_csv(data_loc)

def feature_correlation():
    X = data[[0, 1, 2, 3, 4]].values
    y = data[['outcome']].values.flatten()
    
    p_values = []
    for i in range(5):
        p_values.append(pearsonr(X[:,i], y)[1])
    
    plt.bar(range(len(p_values)), p_values, color='g', alpha=0.5)
    plt.title('Feature correlation')
    plt.ylabel('p-value')
    plt.xlabel('Feature')
    
    
if __name__ == "__main__":
    feature_correlation()      