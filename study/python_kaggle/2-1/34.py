#-*- coding:utf-8 -*-
"""
 Createed by xlj on 2018/2/24
 美国波士顿地区房价数据描述
"""
# 导入波士顿房价数据读取器
from sklearn.datasets import load_boston
# 从读取房价数据存储在变量boston中
boston=load_boston()
#输出数据描述
print (boston.DESCR)