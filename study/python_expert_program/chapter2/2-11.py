#-*- coding:utf-8 -*-
"""
"""
from itertools import groupby
def compress(data):
    return ((len(list(group)),name) for name,group in groupby(data))

def decompress(data):
    return (car*size for size,car in data)


print (list(compress('get uuuuuuuuuuuuuuuuuup')))
compressed=compress('get uuuuuuuuuuuuuuuuuup')
print (''.join(decompress(compressed)))