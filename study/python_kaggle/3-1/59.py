# -*- coding:utf-8 -*-
"""
 Createed by xlj on 2018/2/28
 使用Titanic数据集，通过特征筛选的方法一步步提升决策树的预测性能
"""
import pandas as pd

titanic = pd.read_csv('http://biostat.mc.vanderbilt.edu/wiki/pub/Main/DataSets/titanic.txt')
# 分离数据特征与预测目标
y = titanic['survived']
X = titanic.drop(['row.names', 'name', 'survived'], axis=1)
# 对缺失的数据进行填充
X.fillna('UNKNOWN', inplace=True)

# 分割数据，依然采样25%用于测试
from sklearn.cross_validation import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=33)
# 类别型特征向量化
from sklearn.feature_extraction import DictVectorizer

vec = DictVectorizer()
X_train = vec.fit_transform(X_train.to_dict(orient='record'))
X_test = vec.transform(X_test.to_dict(orient='record'))

# 输出处理后特征向量的维度
print (len(vec.feature_names_))

# 使用决策树模型依靠所有特征进行预测，并作性能评估
from sklearn.tree import DecisionTreeClassifier

dt = DecisionTreeClassifier(criterion='entropy')
dt.fit(X_train, y_train)
print (dt.score(X_test, y_test))

# 导入筛选器
from sklearn import feature_selection

# 筛选钱20%的特征，使用相同配置的决策树模型进行预测，并且评估性能
fs = feature_selection.SelectPercentile(feature_selection.chi2, percentile=20)
X_train_fs = fs.fit_transform(X_train, y_train)
dt.fit(X_train_fs, y_train)
X_test_fs = fs.transform(X_test)
print (dt.score(X_test_fs, y_test))

# 通过交叉验证的方法，按照固定间隔的百分比筛选特征，并作图展示性能随特征筛选比例的变化
from sklearn.cross_validation import cross_val_score
import numpy as np

percentiles = range(1, 100, 2)
results = []

for i in percentiles:
    fs = feature_selection.SelectPercentile(feature_selection.chi2, percentile=i)
    X_train_fs = fs.fit_transform(X_train, y_train)
    scores = cross_val_score(dt, X_train_fs, y_train, cv=5)
    results = np.append(results, scores.mean())

print (results)

# 找到提现最佳性能的特征筛选的百分比
opt = np.where(results == results.max())[0]
# print opt
print ('Optimal number of features %d' % percentiles[opt])
