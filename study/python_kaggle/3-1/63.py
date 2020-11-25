# -*- coding:utf-8 -*-
"""
 Createed by xlj on 2018/3/1
 评估3中回归模型在测试数据集上的性能表现
"""
# 输入训练样本的特征以及目标值，分别存储在变量X_train与y_train中
X_train = [[6], [8], [10], [14], [18]]
y_train = [[7], [9], [13], [17.5], [18]]
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# 使用默认配置初始化线性回归模型
regressor = LinearRegression()
# 直接以披萨的直径作为特征训练模型
regressor.fit(X_train, y_train)

import numpy as np

# 在X轴上从0 到25均匀采样100个数据点
xx = np.linspace(0, 26, 100)
xx = xx.reshape(xx.shape[0], 1)
# 以上述100个数据点作为基准，预测回归直线
yy = regressor.predict(xx)

# 使用PolynomialFeatures（degree=2)映射出2次多项式特征，存储在变量X_train_poly2中
poly2 = PolynomialFeatures(degree=2)
X_train_poly2 = poly2.fit_transform(X_train)
# 以线性回归器为基础，初始化回归模型，尽管特征的维度有提升，但是模型基础仍然是线性模型
regressor_poly2 = LinearRegression()
# 对2次多项式回归模型进行训练
regressor_poly2.fit(X_train_poly2, y_train)
# 重新映射绘图用X轴采样数据
xx_poly2 = poly2.transform(xx)
# 使用2次多项式回归模型对应x轴采样数据进行回归预测
yy_poly2 = regressor_poly2.predict(xx_poly2)

# 使用PolynomialFeatures（degree=4)映射出4次多项式特征，存储在变量X_train_poly4中
poly4 = PolynomialFeatures(degree=4)
X_train_poly4 = poly4.fit_transform(X_train)
# 以线性回归器为基础，初始化回归模型，尽管特征的维度有提升，但是模型基础仍然是线性模型
regressor_poly4 = LinearRegression()
# 对2次多项式回归模型进行训练
regressor_poly4.fit(X_train_poly4, y_train)
# 重新映射绘图用X轴采样数据
xx_poly4 = poly4.transform(xx)
# 使用2次多项式回归模型对应x轴采样数据进行回归预测
yy_poly4 = regressor_poly4.predict(xx_poly4)

# 准备测试数据
X_test = [[6], [8], [11], [16]]
y_test = [[8], [12], [15], [18]]

# 使用测试数据对线性回归模型的性能进行评估
print (regressor.score(X_test, y_test))
# 使用测试数据对2次多项式回归模型的性能进行评估
X_test_ploy2 = poly2.transform(X_test)
print (regressor_poly2.score(X_test_ploy2, y_test))
# 使用测试数据对4次多项式回归模型的性能进行评估
X_test_ploy4 = poly4.transform(X_test)
print (regressor_poly4.score(X_test_ploy4, y_test))
