# -*- coding:utf-8 -*-
"""
 Createed by xlj on 2018/2/24
 对iris数据集进行分割
"""
from sklearn.cross_validation import train_test_split
from sklearn.datasets import load_iris

# 使用加载器读取数据并且存入变量iris
iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.25, random_state=33)
