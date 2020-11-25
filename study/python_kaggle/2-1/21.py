#-*- coding:utf-8 -*-
"""
 Createed by xlj on 2018/2/24
 读取20类新闻文本的数据细节
"""
# 从sklearn.datasets里导入新闻数据抓取器fetch_20newsgroups
from sklearn.datasets import fetch_20newsgroups
# 与之前预存的数据不同，fetch_20newsgroups需要即时从互联网下载数据
news=fetch_20newsgroups(subset='all')
# 查验数据规模和细节
print (len(news.data))
print (news.data[0])