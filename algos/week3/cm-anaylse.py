import numpy as np

labels=["gt", "lt", "eq"]
#cm=[[3202,2192,2625], [2748,2053,2286], [2693,1590,2184]]
cm=[[6793, 4319, 0], [6244, 4051, 0], [  94,   72, 0]]
#cm = [[4550,3619,163], [3952,3352,196], [1682,1289, 70]]
#cm=[[6941,3001,703], [6244,2775,554], [2552,1237,239]]
#cm=[[3202,2192,2625],[2748,2053,2286],[2693,1590,2184]]

#cm = [[3202,2192,2625] ,[2748,2053,2286] ,[2693,1590,2184]]

#when eq range = 0
cm = np.array([[6793,4319, 0], [6244 ,4051, 0], [  94   ,72, 0]])

#cm = np.array([[6696,4265, 0], [6127,3997, 0], [ 297 ,191, 0]])

#cm = [[6696,4265, 0], [6127,3997, 0], [ 297, 191, 0]]

cm = [[4391,1429,2380], [4078,1300,2226], [ 193,  67, 109]]

[[4391 1429 2380]
 [4078 1300 2226]
 [ 193   67  109]]

total = np.sum(cm)

correct_pred_total = 0.0
for i, row in enumerate(cm):
	correct_pred_total += row[i]



print (correct_pred_total / total)

print [(a, np.sum(b)) for a, b in zip(labels, cm)]

#print cm / float(total)