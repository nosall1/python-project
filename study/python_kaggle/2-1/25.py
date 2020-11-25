# -*- coding:utf-8 -*-
"""
 Createed by xlj on 2018/2/24
 读取iris数据集细节资料
"""
from sklearn.datasets import load_iris

# 使用加载器读取数据并且存入变量iris
iris = load_iris()
# 查验数据规模
print (iris.data.shape)
# 查看数据说明
print (iris.DESCR)
