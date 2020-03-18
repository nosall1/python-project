#-*- coding:utf-8 -*-
# 选择排序
import copy
from .data import Data
def selection_sort(data_set):
    frams=[data_set]
    ds=copy.deepcopy(data_set)
    for i in range(0,Data.data_count-1):
        for j in range(i+1,Data.data_count):
            ds_r=copy.deepcopy(ds)
            frams.append(ds_r)
            ds_r[i].set_color('r')
            ds_r[j].set_color('k')

            if ds[j].value<ds[i].value:
                ds[i],ds[j]=ds[j],ds[i]

    frams.append(ds)
    return frams

