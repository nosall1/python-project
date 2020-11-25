# -*- coding:utf-8 -*-
"""
 Createed by xlj on 2018/3/8
 使用skflow内置的LinearRegressor，DNN已经Scikit-learn中的集成回归模型对‘美国波士顿房价'数据进行回归预测
"""
from sklearn import datasets, metrics, preprocessing, cross_validation

# 使用datasets.load_boston读取美国波士顿房价数
boston = datasets.load_boston()

# 获取房屋数据特征以及对应房价
X, y = boston.data, boston.target

# 分割数据，随机采样25%作为测试样本
X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.25, random_state=33)

# 对数据特征进行标准化处理
scaler = preprocessing.StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

import skflow

# 使用skflow的LinearRegressor
tf_lr = skflow.TensorFlowLinearRegressor(steps=10000, learning_rate=0.01, batch_size=50)
tf_lr.fit(X_train, y_train)
tf_lr_y_predict = tf_lr.predict(X_test)

# 输出skflow中的LinearRegressor模型的回归性能
print ('The mear absoluate error of Tensorflow Linear Regressor on boston dataset is ', metrics.mean_absolute_error(
    tf_lr_y_predict, y_test))
print ('The mean squared error of Tensorflow Linear Regressor on boston dataset is ', metrics.mean_squared_error(
    tf_lr_y_predict, y_test))
print ('The R-squared value of Tensorflow Linear Regressor on boston dataset is ', metrics.r2_score(tf_lr_y_predict,
                                                                                                   y_test))
