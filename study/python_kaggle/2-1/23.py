#-*- coding:utf-8 -*-
"""
 Createed by xlj on 2018/2/24
 使用朴素贝叶斯分类器对新闻文本数据进行类别预测
"""
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cross_validation import train_test_split
from sklearn.datasets import fetch_20newsgroups
# 从sklearn.naive_bayes里导入朴素贝叶斯模型
from sklearn.naive_bayes import MultinomialNB
# 与之前预存的数据不同，fetch_20newsgroups需要即时从互联网下载数据
news=fetch_20newsgroups(subset='all')
# 随机采样25%的数据样本作为测试集
X_train,X_test,y_train,y_test=train_test_split(news.data,news.target,test_size=0.25,random_state=33)
vec=CountVectorizer()
X_train=vec.fit_transform(X_train)
X_test=vec.transform(X_test)
mnb=MultinomialNB()
# 利用训练数据对模型参数进行估计
mnb.fit(X_train,y_train)
# 对测试样本进行类别预测，结果存储在变量y_predict中
y_predict=mnb.predict(X_test)

