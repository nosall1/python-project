#-*- coding:utf-8 -*-
"""
 Createed by xlj on 2018/2/24
 手写体数据分割代码样例
"""

# 从sklearn.cross_validation中导入train_test_split用于数据分割
from sklearn.cross_validation import train_test_split

# 从sklearn.datasets里导入手写体数字加载器
from sklearn.datasets import load_digits
# 从通过数据加载器获得手写体数字的数码图像数据并存储在digits变量中
digits=load_digits()
# 检视数据规模和特征维度
# print digits.data.shape
# 随机选取75%的数据作为训练样本，其余25%的数据作为测试样本
X_train,X_test,y_train,y_test=train_test_split(digits.data,digits.target,test_size=0.25,random_state=33)
# 分别检视训练和测试数据规模
print( y_train.shape)
print (y_test.shape)