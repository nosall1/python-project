#-*- coding:utf-8 -*-
"""
 Createed by xlj on 2018/2/24
 20类新闻文本数据分割
"""
from sklearn.cross_validation import train_test_split
from sklearn.datasets import fetch_20newsgroups
# 与之前预存的数据不同，fetch_20newsgroups需要即时从互联网下载数据
news=fetch_20newsgroups(subset='all')
# 随机采样25%的数据样本作为测试集
X_train,X_test,y_train,y_test=train_test_split(news.data,news.target,test_size=0.25,random_state=33)