#coding=utf-8
__author__= 'wenqifan'

import sys
import time
import logging
import argparse
from collections import defaultdict

import numpy as np
import scipy
from sklearn.metrics import roc_auc_score
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

logger = logging.getLogger("Basic")
logger.setLevel(logging.INFO)
stdout_handler = logging.StreamHandler(sys.stderr)
formatter = logging.Formatter("%(asctime)s:%(levelname)s:%(message)s")
stdout_handler.setFormatter(formatter)
logger.addHandler(stdout_handler)

def sample_from_file(sample_file, n_samples):
    sampled_set = [None] * n_samples
    with open(sample_file, 'r') as f:
        for i, line in enumerate(f):
            if i < n_samples:
                sampled_set[i] = line
            else:
                r = np.random.randint(0, i)
                if r < n_samples:
                    sampled_set[r] = line
    return sampled_set

def load_data(sample_file=None, train_sample_file=None, test_sample_file=None, n_samples=1000000, test_ratio=0.3):
    if sample_file is not None:
        sampled_set = sample_from_file(sample_file, n_samples)
        Train, Test = train_test_split(sampled_set, test_size=test_ratio)
    elif train_sample_file is not None and test_sample_file is not None:
        Train = sample_from_file(train_sample_file, n_samples)
        Test = sample_from_file(train_sample_file, n_samples)



    train_row_dict, train_col_dict = defaultdict(list), defaultdict(list)
    test_row_dict, test_col_dict = defaultdict(list), defaultdict(list)
    feaid_dict = defaultdict(dict)
    feaid_dict_cnt = defaultdict(int)
    train_labels, test_labels = np.zeros(len(Train)), np.zeros(len(Test))
    train_cnt, test_cnt = 0, 0
    for i, line in enumerate(Test):
        splited = line.split(' ')
        label, feature = splited[1], splited[2:]
        test_labels[i] = int(label)
        for j in xrange(len(feature)):
            feature_id = feature[j].split(":")[0]
            feature_id_int = int(feature_id)
            group_id = feature_id_int % 1000
            if feature_id not in feaid_dict[group_id]:
                feaid_dict[group_id][feature_id] = feaid_dict_cnt[group_id]
                feaid_dict_cnt[group_id] += 1
            test_col_dict[group_id].append(feaid_dict[group_id][feature_id])
            test_row_dict[group_id].append(test_cnt)
        test_cnt += 1
    for i, line in enumerate(Train):
        splited = line.split(' ')
        label, feature = splited[1], splited[2:]
        train_labels[i] = int(label)
        for j in xrange(len(feature)):
            feature_id = feature[j].split(":")[0]
            feature_id_int = int(feature_id)
            group_id = feature_id_int % 1000
            if feature_id not in feaid_dict[group_id]:
                feaid_dict[group_id][feature_id] = feaid_dict_cnt[group_id]
                feaid_dict_cnt[group_id] += 1
            train_col_dict[group_id].append(feaid_dict[group_id][feature_id])
            train_row_dict[group_id].append(train_cnt)
        train_cnt += 1
    X_train_dict, X_test_dict = defaultdict(scipy.sparse.csr_matrix), defaultdict(scipy.sparse.csr_matrix)
    for k, v in train_col_dict.iteritems():
        data = np.ones(len(train_col_dict[k]))
        train_row, train_col = train_row_dict[k], train_col_dict[k]
        features_num = len(feaid_dict[k].keys())
        X_train_dict[k] = scipy.sparse.csr_matrix(scipy.sparse.coo_matrix((data, (train_row, train_col)), shape=(train_cnt, features_num)))
    for k, v in test_col_dict.iteritems():
        data = np.ones(len(test_col_dict[k]))
        test_row, test_col = test_row_dict[k], test_col_dict[k]
        features_num = len(feaid_dict[k].keys())
        X_test_dict[k] = scipy.sparse.csr_matrix(scipy.sparse.coo_matrix((data, (test_row, test_col)), shape=(test_cnt, features_num)))
    y_train, y_test = np.asarray(train_labels), np.asarray(test_labels)
    return X_train_dict, X_test_dict, y_train, y_test

def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command")
    subparser_all = subparsers.add_parser("a")
    subparser_all.add_argument("--name")
    subparser_all.add_argument("--n", type=int)
    subparser_all.add_argument("--ratio", type=float)
    subparser_train_test = subparsers.add_parser("t")
    subparser_train_test.add_argument("--train_name")
    subparser_train_test.add_argument("--test_name")
    subparser_train_test.add_argument("--n", type=int)
    subparser_train_test.add_argument("--ratio", type=float)
    args = parser.parse_args()
    if args.command == "a":
        X_train, X_test, y_train, y_test = load_data(sample_file=args.name, n_samples=args.n, test_ratio=args.ratio)
    elif args.command == "t":
        X_train, X_test, y_train, y_test = load_data(train_sample_file=args.train_name,
                test_sample_file=args.test_name, n_samples=args.n, test_ratio=args.ratio)
    else:
        raise ValueError

    print "Group_id, Auc"
    for k, v in X_train.items():
        start_time = time.time()
        lr_model = LogisticRegression()
        lr_model.fit(v, y_train)
        pr = lr_model.predict(X_test[k])
        auc = roc_auc_score(y_test, pr)
        logger.info("Group %s Evaluted, AUC=%f, Time Cost: %f" % (k, auc, time.time()-start_time))
        print "%s, %f" % (k, auc)

if __name__ == '__main__':
    logger.info("Evaluation Started...")
    start_time = time.time()
    main()
    logger.info("Evaluation Finished\nTime cost: %s" % str(time.time()-start_time))

