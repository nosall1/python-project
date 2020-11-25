# -*- coding:utf-8 -*-
"""
 Createed by xlj on 2018/3/1
 使用2次多项式回归模型在披萨训练样本上进行拟合
"""
# 导入多项式特征产生器
from sklearn.preprocessing import PolynomialFeatures

X_train = [[6], [8], [10], [14], [18]]
y_train = [[7], [9], [13], [17.5], [18]]
from sklearn.linear_model import LinearRegression

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
# 分别对训练数据点、线性回归直线，2次多项式回归曲线进行作图
import matplotlib.pyplot as plt

plt.scatter(X_train, y_train)
plt1, = plt.plot(xx, yy, label='Degree=1')
plt2, = plt.plot(xx, yy_poly2, label='Degree=2')
plt.axis([0, 25, 0, 25])
plt.xlabel('Diameter of Pizza')
plt.ylabel('Price of Pizza')
plt.legend(handles=[plt1, plt2])
plt.show()
# 输出线性回归模型在训练样本上的R-squared值
print ('The R-squared value of Liner Regressor(Degree=2) performing on training data is', regressor_poly2.score(X_train_poly2, y_train))
