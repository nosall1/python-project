#-*- coding:utf-8 -*-

import copy
from .data import Data
# 插入排序

def insertion_sort(data_set):
    frames=[data_set]
    ds=copy.deepcopy(data_set)
    for i in range(1,Data.data_count):
        frames.append(copy.deepcopy(ds))
        frames[-1][i].set_color('r')
        for j in range(i,0,-1):
            if ds[j].value<ds[j-1].value:
                ds[j],ds[j-1]=ds[j-1],ds[j]

                frames.append(copy.deepcopy(ds))
                frames[-1][j-1].set_color('r')

            else:
                break
    frames.append(ds)
    return frames