# -*- coding:utf-8 -*-
"""
 Createed by xlj on 2018/2/23
"""
# 使用sklearn.cross_valiation里的train_test_split模块用于分割数据
from sklearn.cross_validation import train_test_split
import pandas as pd
import numpy as np

# 创建特征列表
column_names = ['Sample code number', 'Clump Thickness', 'Uniformity of Cell Size',
                'Uniformity of Cell Shape', 'Marginal Adhesion', 'Single Epithelial Cell Size',
                'Bare Nuclei', 'Bland Chromatin', 'Normal Nucleoli', 'Mitoses', 'Class']

# 使用pandas.read_csv函数从互联网读取指定数据
data = pd.read_csv(
    'https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data',
    names=column_names)
# 将？替换为标准缺失值表示
data = data.replace(to_replace='?', value=np.nan)
# 丢弃带有缺失值的数据（只要有一个维度有缺失）
data = data.dropna(how='any')
# 随机采样25%的数据用于测试，剩下的75%用于构建训练集合
X_train, X_test, y_train, y_test = train_test_split(data[column_names[1:10]], data[column_names[10]], test_size=0.25,
                                                    random_state=33)
# 查验训练样本的数量和类别分布
print (y_train.value_counts())
# 查验测试样本的数量和类别分布
print (y_test.value_counts())
