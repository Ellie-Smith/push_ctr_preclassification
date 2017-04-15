#coding=utf-8
import numpy as np
from collections import Counter

def entropy(D):
    count_array=np.array(Counter(D).values())
    P=count_array/float(count_array.sum())
    H=np.dot(-P,np.log2(P))
    return H

def condition_entropy(D,A):
    A=np.array(A)
    D=np.array(D)
    H_da=0
    for i in np.unique(A):
        index_i=np.ravel(np.argwhere(A==i))
        Di=D[index_i]
        H_Di=entropy(Di)
        pi=float(Di.size)/D.size
        H_da=H_da+pi*H_Di
    return H_da


x1=[0,0,0,0,0,1,1,1,1,1,2,2,2,2,2]
x2=[0,0,1,1,0,0,0,1,0,0,0,0,1,1,0]
x3=[0,0,0,1,0,0,0,1,1,1,1,1,0,0,0]
x4=[0,1,1,0,0,0,1,1,2,2,2,1,1,2,0]
y =[0,0,1,1,0,0,0,1,1,1,1,1,1,1,0]

X=np.c_[x1,x2,x3,x4]
y=np.array(y)
Hy=entropy(y)
Hyx1=condition_entropy(y,x1)
Hyx2=condition_entropy(y,x2)
Hyx3=condition_entropy(y,x3)
Hyx4=condition_entropy(y,x4)

g_yx1=Hy-Hyx1
g_yx2=Hy-Hyx2
g_yx3=Hy-Hyx3
g_yx4=Hy-Hyx4

print Hy  #熵 H(y)
print Hyx1   #条件熵 H(y|x1)
print Hyx2
print Hyx3
print Hyx4

print g_yx1 #信息增益g(y,x1)
print g_yx2
print g_yx3
print g_yx4
