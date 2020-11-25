# -*- coding:utf-8 -*-
"""
 Createed by xlj on 2018/2/24
 使用线性回归模型LinearRegression和SGCRegressor分别对美国波士顿地区房价进行预测
"""
from sklearn.linear_model import LinearRegression

# 导入数据标准化模块
from sklearn.preprocessing import StandardScaler
from sklearn.cross_validation import train_test_split
import numpy as np
from sklearn.datasets import load_boston

# 从读取房价数据存储在变量boston中
boston = load_boston()
# 输出数据描述
X = boston.data
y = boston.target

# 随机采样25%的数据构建测试样本，其余作为训练样本
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=33, test_size=0.25)
# 分别初始化对特征和目标值的标准化器
ss_X = StandardScaler()
ss_y = StandardScaler()
# 分别对训练和测试数据的特征以及目标值进行标准化处理
X_train = ss_X.fit_transform(X_train)
X_test = ss_X.transform(X_test)
y_train = ss_y.fit_transform(y_train)
y_test = ss_y.transform(y_test)
# 使用默认配置初始化线性回归器
lr = LinearRegression()  # 使用训练数据进行参数估计
lr.fit(X_train, y_train)
# 对测试数据进行回归预测
lr_y_predict = lr.predict(X_test)

from sklearn.linear_model import SGDRegressor

# 使用默认配置初始化线性回归器SGDRegressor
sgdr = SGDRegressor()
# 使用训练数据进行参数估计
sgdr.fit(X_train, y_train)
# 对测试数据进行回归预测
sgdr_y_predict = sgdr.predict(X_test)
