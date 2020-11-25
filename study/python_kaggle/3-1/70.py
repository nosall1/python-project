# -*- coding:utf-8 -*-
"""
 Createed by xlj on 2018/3/2
 使用NLTk对示例文本进行语言分析
"""
import nltk

sent1 = 'The cat is walking in the bedroom.'
sent2 = 'A dog was running across the kitchen.'
# 对句子进行词汇分割和正规化，有些情况如are't需要分割为are和n't;或者I'm需分割为I和'm
tokens_1 = nltk.word_tokenize(sent1)
print (tokens_1)
tokens_2 = nltk.word_tokenize(sent2)
print (tokens_2)
# 整理两句的词表，并且按照ascii的排序输出
vocab_1 = sorted(set(tokens_1))
print (vocab_1)
vocab_2 = sorted(set(tokens_2))
print (vocab_2)

# 初始化stemmer寻找各个词汇最原始的词根
stemmer = nltk.stem.PorterStemmer()
stem_1 = [stemmer.stem(t) for t in tokens_1]
print (stem_1)

stem_2 = [stemmer.stem(t) for t in tokens_2]
print (stem_2)

# 初始化词性标注器，对每个词汇进行标注
pos_tag_1 = nltk.tag.pos_tag(tokens_1)
print (pos_tag_1)
pos_tag_2 = nltk.tag.pos_tag(tokens_2)
print (pos_tag_2)
