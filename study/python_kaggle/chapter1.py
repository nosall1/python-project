# -*- coding:utf-8 -*-
"""
 Createed by xlj on 2018/2/22
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# 导入sklearn中的逻辑斯蒂回归分类器
from sklearn.linear_model import LogisticRegression

# 传入训练文件地址参数
df_train = pd.read_csv('./Datasets/Breast-Cancer/breast-cancer-train.csv')
# 传入测试文件地址参数
df_test = pd.read_csv('./Datasets/Breast-Cancer/breast-cancer-test.csv')
# 选取'Clump Thickness' 与'cell Size'作为特征，构建测试集中的正负分类样本
df_test_negative = df_test.loc[df_test['Type'] == 0][['Clump Thickness', 'Cell Size']]
df_test_positive = df_test.loc[df_test['Type'] == 1][['Clump Thickness', 'Cell Size']]

# 绘制图1-2中的良性肿瘤样本点，标记为红色的o
plt.scatter(df_test_negative['Clump Thickness'], df_test_negative['Cell Size'], marker='o', s=200, c='red')
# 绘制图1-2中的恶性肿瘤样本点，标记为黑色的x
plt.scatter(df_test_positive['Clump Thickness'], df_test_positive['Cell Size'], marker='x', s=200, c='black')

# 绘制x,y轴的说明
plt.xlabel('Clump Thickness')
plt.ylabel('Cell Size')
# 显示图像
plt.show()

# 利用numpy中的random函数随机采样直线的截距和系数
intercept = np.random.random([1])
coef = np.random.random([2])
lx = np.arange(0, 12)
ly = (-intercept - lx * coef[0]) / coef[1]
# 绘制一条随机直线
plt.plot(lx, ly, c='yellow')

# 绘制图1-3
plt.scatter(df_test_negative['Clump Thickness'], df_test_negative['Cell Size'], marker='o', s=200, c='red')
plt.scatter(df_test_positive['Clump Thickness'], df_test_positive['Cell Size'], marker='x', s=200, c='black')
plt.xlabel('Clump Thickness')
plt.ylabel('Cell Size')
plt.show()

lr = LogisticRegression()
# 使用前10条训练样本学习直线的系数和截距
lr.fit(df_train[['Clump Thickness', 'Cell Size']][:10], df_train['Type'][:10])
print 'Testing accuracy (10 traing samples):', lr.score(df_test[['Clump Thickness', 'Cell Size']], df_test['Type'])

intercept = lr.intercept_
coef = lr.coef_[0, :]
# 原本这个分类面应该是lx_coef[0+ly*coef[1]+intercept=0,映射到2唯平面上之后，应该是：
ly = (-intercept - lx * coef[0]) / coef[1]
# 绘制图1-4
plt.plot(lx, ly, c='green')
plt.scatter(df_test_negative['Clump Thickness'], df_test_negative['Cell Size'], marker='o', s=200, c='red')
plt.scatter(df_test_positive['Clump Thickness'], df_test_positive['Cell Size'], marker='x', s=200, c='black')
plt.xlabel('Clump Thickness')
plt.ylabel('Cell Size')
plt.show()

lr = LogisticRegression()
# 使用所有训练样本学习直线的系数和截距
lr.fit(df_train[['Clump Thickness', 'Cell Size']], df_train['Type'])
print 'Testing accuracy (all training samples):', lr.score(df_test[['Clump Thickness', 'Cell Size']], df_test['Type'])
intercept = lr.intercept_
coef = lr.coef_[0, :]
ly = (-intercept - lx * coef[0]) / coef[1]

# 绘制图1-5
plt.plot(lx, ly, c='blue')
plt.scatter(df_test_negative['Clump Thickness'], df_test_negative['Cell Size'], marker='o', s=200, c='red')
plt.scatter(df_test_positive['Clump Thickness'], df_test_positive['Cell Size'], marker='x', s=200, c='black')
plt.xlabel('Clump Thickness')
plt.ylabel('Cell Size')
plt.show()
