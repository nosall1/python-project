# -*- coding:utf-8 -*-
"""
 Createed by xlj on 2018/2/24
 美国波士顿地区房价数据分割
"""
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

# 分析回归目标值的差异
print ('The max target value is ', np.max(boston.target))
print ('The min target value is ', np.min(boston.target))
print ('The average target value is ', np.mean(boston.target))
