#coding=utf-8
# 1 政治
# 2 娱乐
# 3 幽默
# 4 体育
# 5 时尚
# 6 生活
# 7 社会
# 8 人际关系
# 9 汽车
# 10 奇闻异事
# 11 其他
# 12 科学
# 13 科技
# 14 经济
# 15 健康
# 16 观点
# 17 异常

from sklearn import svm
from sklearn.linear_model import LogisticRegression
from sklearn import tree
from sklearn.datasets import load_iris
from sklearn import preprocessing
import random

# load the dataset

ctr_train = load_iris('train5.csv')
ctr_test = load_iris('test5.csv')
# ctr_train_data = preprocessing.scale(ctr_train.data)
# ctr_test_data = preprocessing.scale(ctr_test.data)
ctr_train_data = ctr_train.data
ctr_test_data = ctr_test.data

print type(ctr_test_data)

def svmClassifier(data,target):
    clf = svm.SVC()
    clf.fit(data,target)
    return clf

def LRClassifier(data,target):
    clf = LogisticRegression()
    clf.fit(data, target)
    return clf
#max_depth=10,min_samples_leaf=1000
def TreeClassifier(data,target,max_depth,min_samples_leaf,min_samples_split):
    clf = tree.DecisionTreeClassifier(criterion='gini',max_depth=max_depth,min_samples_leaf=min_samples_leaf,min_samples_split=min_samples_split,)
    clf = clf.fit(data, target)
    return clf

def getResult(predict_list,label):
    TP,FP,TN,FN=0,0,0,0
    for i in range(len(predict_list)):
        if predict_list[i] == 1 and label[i] == 1:
            TP += 1
        elif predict_list[i] == 1 and label[i] == 0:
            FP += 1
        elif predict_list[i] == 0 and label[i] == 1:
            FN += 1
        else:
            TN += 1
    print 'TP: ',TP,'TN: ',TN,'FP: ',FP,'FN: ',FN
    if TP+FP == 0:
        percision = 0
    else:
        percision = float(TP)/(TP+FP)
    if TP+FN == 0:
        recall = 0
    else:
        recall = float(TP)/(TP+FN)
    if percision+recall == 0:
        F1 = 0
    else:
        F1 = 2*percision*recall/(percision+recall)
    print F1,percision,recall
    return percision,recall,F1


best = {'percision':0,'recall':0,'f1':0,'depth':0,'min_samples_leaf':0}

for depth in range(1,8):
    min_samples_leaf = 70
    while min_samples_leaf > 5:
        predict = []
        # classifier = TreeClassifier(ctr_train_data,ctr_train.target,depth,min_samples_leaf,2*min_samples_leaf)
        classifier = svmClassifier(ctr_train_data,ctr_train.target)
        for i in range(len(ctr_test_data)):
            predict.append(classifier.predict([ctr_test_data[i]]))
            # if ctr_test_data[i][3]>0.11 and ctr_test_data[i][1]>3000:
            #     predict.append(1)
            # else:
            #     predict.append(0)
            # print classifier.predict([ctr_test_data[i]]),ctr_test.target[i]

        p,r,f1 = getResult(predict,ctr_test.target)
        if f1>best['f1']:
            best['f1'] = f1
            best['percision'] = p
            best['recall'] = r
            best['depth'] = depth
            best['min_samples_leaf'] = min_samples_leaf
        # print p,r,f1
        # print depth,min_samples_leaf
        # print '----------------'
        min_samples_leaf -= 5
print best



# predict = []
# classifier = TreeClassifier(ctr_train_data,ctr_train.target,5,30,60)
# # classifier = TreeClassifier(ctr_train_data,ctr_train.target)
# for i in range(len(ctr_test_data)):
#         predict.append(classifier.predict([ctr_test_data[i]]))
#   # predict.append(random.randint(0, 1))
# p,r,f1 = getResult(predict,ctr_test.target)
# print p,r,f1
# print '----------------'
#
# with open("ctr.dot", 'w') as f:
#     f = tree.export_graphviz(classifier, out_file=f)