#-*- coding:utf-8 -*-
"""
 Createed by xlj on 2018/2/24
 手写体数据读取代码样例
"""
# 从sklearn.datasets里导入手写体数字加载器
from sklearn.datasets import load_digits
# 从通过数据加载器获得手写体数字的数码图像数据并存储在digits变量中
digits=load_digits()
# 检视数据规模和特征维度
print (digits.data.shape)