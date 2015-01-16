import pandas as pd
import numpy as np
from sklearn.metrics import confusion_matrix

def discretize(d):
    if d > 0:
        return 1
    elif d == 0:
        return 0
    else:
        return -1

spy = pd.read_csv('ibm.csv')['Close'].values[::-1]

y_true = map(discretize, np.diff(spy[1:]))
y_pred = map(discretize, np.diff(spy[:-1]))

cm = confusion_matrix(y_true, y_pred, labels=[1,-1, 0])

total = np.sum(cm)
correct_pred_total=0.0
for i, row in enumerate(cm):
    correct_pred_total += row[i]   

print("\n" + str(cm))
print("accuracy: " + str(correct_pred_total / total))
print("condition counts: " + str(np.sum(cm, axis=0)))
print("condition prcnts: " + str(100.0 * np.sum(cm, axis=0) / total))
