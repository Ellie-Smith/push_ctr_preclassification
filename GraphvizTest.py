#coding=utf-8
from sklearn.datasets import load_iris
import random
from sklearn import tree


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



ctr_train = load_iris('ctr(send,open,ctr).csv')
ctr_test = load_iris('ctr_test(send,open,ctr).csv')

clf = tree.DecisionTreeClassifier()

clf = clf.fit(ctr_train.data, ctr_train.target)

# export the tree in Graphviz format using the export_graphviz exporter

with open("ctr.dot", 'w') as f:
    f = tree.export_graphviz(clf, out_file=f)
print len(ctr_test.data)
predict = []
for i in range(len(ctr_test.data)):
    predict.append(clf.predict(ctr_test.data[i]))

    # predict.append(random.randint(0,1))



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
    percision = float(TP)/(TP+FP)
    recall = float(TP)/(TP+FN)
    F1 = 2*percision*recall/(percision+recall)
    return percision,recall,F1

p,r,f1 = getResult(predict,ctr_test.target)
print p,r,f1



# print ctr_test.data[1]


