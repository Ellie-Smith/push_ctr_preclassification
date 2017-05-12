#coding=utf-8
import numpy as np
from sklearn.datasets import load_iris

# sigmoid function
def nonlin(x, deriv=False):
    if (deriv == True):
        return x * (1 - x)
    return 1 / (1 + np.exp(-x))


# input dataset
X = np.array([[0, 0, 1],
              [0, 1, 1],
              [1, 0, 1],
              [1, 1, 1]])
ctr_train = load_iris('train4.csv')
ctr_test = load_iris('test4.csv')
# ctr_train_data = preprocessing.scale(ctr_train.data)
# ctr_test_data = preprocessing.scale(ctr_test.data)
ctr_train_data = ctr_train.data
ctr_test_data = ctr_test.data

# output dataset
y = np.array([[0, 0, 1, 1]]).T

# seed random numbers to make calculation
# deterministic (just a good practice)
np.random.seed(1)

# initialize weights randomly with mean 0
syn0 = 2 * np.random.random((5, 1345)) - 1

for iter in xrange(10000):
    # forward propagation
    l0 = ctr_train_data
    l1 = nonlin(np.dot(l0, syn0))

    # how much did we miss?
    l1_error = ctr_train.target - l1

    # multiply how much we missed by the
    # slope of the sigmoid at the values in l1
    l1_delta = l1_error * nonlin(l1, True)

    # update weights
    syn0 += np.dot(l0.T, l1_delta)
print "Output After Training:"
print l1