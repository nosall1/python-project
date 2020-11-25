#-*- coding:utf-8 -*-
"""
 餐饮销量数据相关性分析
"""
import pandas as pd

catering_sale ='./data/catering_sale_all.xls'
data=pd.read_excel(catering_sale,index_col=u'日期')
print(data.corr()) #相关系数矩阵，即给出了任务两款菜式之间的相关系数
print ('-----')
print (data.corr()[u'百合酱蒸凤爪']) #只显示百合酱蒸凤爪与其他菜式的相关系数
print (data[u'百合酱蒸凤爪'].corr(data[u'翡翠蒸香茜饺'])) # 计算 百合酱蒸凤爪 和翡翠蒸香茜饺 的相关系数