# -*- coding:utf-8 -*-
"""
 Createed by xlj on 2018/3/1
 使用词袋法对示例文本进行特征向量化
"""
sent1 = 'The cat is walking in the bedroom'
sent2 = 'A dog was running across the kitchen'

from sklearn.feature_extraction.text import CountVectorizer

count_vec = CountVectorizer()
sentences = [sent1, sent2]
print (count_vec.fit_transform(sentences).toarray())

# 输出向量各个维度的特征含义
print (count_vec.get_feature_names())
