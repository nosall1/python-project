#-*- coding:utf-8 -*-
"""
 Createed by xlj on 2018/2/24
 泰坦尼克号乘客数据查验
"""
import pandas as pd
titanic=pd.read_csv('http://biostat.mc.vanderbilt.edu/wiki/pub/Main/DataSets/titanic.txt')
# 观察前几行数据，可以发发现，数据种类各异，数值型，类别型，甚至还有缺失数据
# print titanic.head()
# 使用pandas，数据都转入pandas独有的dataframe格式（二维数据表格）,直接使用info(),查看数据的统计特性
print (titanic.info())