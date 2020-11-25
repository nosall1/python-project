# -*- coding:utf-8 -*-
"""
 Createed by xlj on 2018/2/24
  K-means算法在手写体数字图像数据上的使用示例
"""
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# 使用pandas分别读取训练数据和测试数据集
digits_train = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/optdigits/optdigits.tra',
                           header=None)
digits_test = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/optdigits/optdigits.tes',
                          header=None)

# 从训练与测试数据集上都分离出64维度的像素特征与1维度的数字目标
X_train = digits_train[np.arange(64)]
y_train = digits_test[64]

X_test = digits_test[np.arange(64)]
y_test = digits_test[64]

from sklearn.cluster import KMeans

# 初始化KMeans模型，并设置聚类中心数量为10
kmeans = KMeans(n_clusters=10)
kmeans.fit(X_train)
# 逐条判断每个测试图像所属的聚类中心
y_pred = kmeans.predict(X_test)
