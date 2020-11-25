#-*- coding:utf-8 -*-
"""
 Createed by xlj on 2018/2/28
 使用TfidfVectorizer并且不去掉停用词的条件下，对文本特征进行量化的朴素贝叶斯分类性能测试
"""
# 从sklearn.datasets里导入20类新闻文本数据抓取器
from sklearn.datasets import fetch_20newsgroups

# 从互联网上即时下载新闻样本，subset='all'参数代表下载全部近2万条文本存储在变量news中
news = fetch_20newsgroups(subset='all')
# 导入train_test_split模块用于分割数据集
from sklearn.cross_validation import train_test_split

# 对news中的数据data进行分割，25%的文本用作测试集，75%作为训练集
X_train, X_test, y_train, y_test = train_test_split(news.data, news.target, test_size=0.25, random_state=33)
from sklearn.feature_extraction.text import TfidfVectorizer
tfidf_vec=TfidfVectorizer()

#使用tfidf的方式，将原始训练和测试文本转化为特征向量
X_tfidf_train=tfidf_vec.fit_transform(X_train)
X_tfidf_test=tfidf_vec.transform(X_test)
# 导入朴素贝叶斯分类器
from sklearn.naive_bayes import MultinomialNB

# 使用默认配置进行初始化
mnb_tfidf = MultinomialNB()
mnb_tfidf.fit(X_tfidf_train,y_train)
print ('The accuracy of classifying 20newsgroups using Naive Bayes(CountVectorizer without filtering stopwords):', mnb_tfidf.score(
    X_tfidf_test, y_test))
# 将分类预测的结果存储在变量y_count_predict中
y_count_predict = mnb_tfidf.predict(X_tfidf_test)
# 导入classification_report
from sklearn.metrics import classification_report

# 输出更加详细的其他评价分类性能的指标
print (classification_report(y_test, y_count_predict, target_names=news.target_names))