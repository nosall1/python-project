#-*- coding:utf-8 -*-
"""
"""
seq=['one','two','three']
for i,element in enumerate(seq):
    seq[i]='%d:%s'%(i,seq[i])
print (seq)