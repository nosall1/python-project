#-*- coding:utf-8 -*-
"""
 Createed by xlj on 2018/2/26
 使用原始像素特征和经PCA压缩重建的低纬特征，在相同配置的支持向量机（分类）模型上分别进行图像识别
"""
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
# 下载训练数据
digits_train = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/optdigits/optdigits.tra',
                           header=None)
# 下载测试数据
digits_test = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/optdigits/optdigits.tes',
                          header=None)

# 分割训练数据的特征向量和标记
X_train = digits_train[np.arange(64)]
y_train = digits_train[64]
X_test=digits_test[np.arange(64)]
y_test=digits_test[64]

# 导入基于线性核的支持向量机分类器
from sklearn.svm import LinearSVC

# 使用默认配置初始化LinearSVC，对原始六十四维像素特征的训练数据y_predict中
svc=LinearSVC()
svc.fit(X_train,y_train)
y_predict=svc.predict(X_test)

#使用PCA将原64维的图像数据压缩到20个维度
estimator=PCA(n_components=20)

# 利用训练特征决定（fit)20个正交维度的方向，并转化（transform)原训练特征
pca_x_train=estimator.fit_transform(X_train)
# 测试特征也按照上述的20个正交维度方向进行转化（transform)
pca_x_test=estimator.transform(X_test)
# 使用默认配置初始化LinearSVC，对压缩过后的20维特征的训练数据进行建模，并在测试数据上做出预测，存储在pca_y_predict中
pca_svc=LinearSVC()
pca_svc.fit(pca_x_train,y_train)
pca_y_predict=pca_svc.predict(pca_x_test)