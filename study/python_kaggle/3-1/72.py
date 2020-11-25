# -*- coding:utf-8 -*-
"""
 Createed by xlj on 2018/3/2
 对比随机决策森林以及XGBoost模型对泰坦尼克号上的乘客是否生还的预测能力
"""
import pandas as pd

titanic = pd.read_csv('http://biostat.mc.vanderbilt.edu/wiki/pub/Main/DataSets/titanic.txt')

# 选取pclass,age以及sex作为训练特征
X = titanic[['pclass', 'age', 'sex']]
y = titanic['survived']

# 对缺失的age信息，采用平均值方法进行补全，即以age列已知数据的平均数填充
X['age'].fillna(X['age'].mean(), inplace=True)
# 对原始数据进行分割，随机采样25%作为测试集
from sklearn.cross_validation import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=33)

from sklearn.feature_extraction import DictVectorizer

vec = DictVectorizer(sparse=False)

# 对原数据进行特征向量化处理
X_train = vec.fit_transform(X_train.to_dict(orient='record'))
X_test = vec.transform(X_test.to_dict(orient='record'))

# 采用默认配置的随机森林分类器对测试集进行预测
from sklearn.ensemble import RandomForestClassifier

rfc = RandomForestClassifier()
rfc.fit(X_train, y_train)
print ('The accuracy of Random Forest Classifier on testing set:', rfc.score(X_test, y_test))
