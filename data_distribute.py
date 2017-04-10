#coding=utf-8
from matplotlib import pyplot as plt
import matplotlib
from sklearn.datasets import load_iris
import numpy as np

plt.figure(figsize=(9,6))
axes = plt.subplot(111)

# ctr_train = load_iris('ctr1(send,open,ctr).csv')
# ctr_train = load_iris('ctr(send,open,ctr).csv')
ctr_train = load_iris('train2.csv')
type1_x,type1_y,type2_x,type2_y = [],[],[],[]
for i in range(len(ctr_train.data)):
    if ctr_train.target[i] == 0:
        # if ctr_train.data[i][1] < 200000 and ctr_train.data[i][3] < 0.17:
        #     type2_x.append(ctr_train.data[i][1])
        #     type2_y.append(ctr_train.data[i][3])
        pass

    else:
        if ctr_train.data[i][1] < 200000 and ctr_train.data[i][3] < 0.17:
            type1_x.append(ctr_train.data[i][1])
            type1_y.append(ctr_train.data[i][3])
        # pass

type1 = axes.scatter(type1_x, type1_y,s=40, c='yellow' )
type2 = axes.scatter(type2_x, type2_y, s=40, c='blue')

axes.legend((type1, type2), ('0', '1'),loc=1)


plt.show()




