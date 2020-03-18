#-*- coding:utf-8 -*-

import copy
from .data import Data
# 梳排序
def comb_sort(data_set):
    frames=[data_set]
    ds=copy.deepcopy(data_set)
    div=int(Data.data_count/1.3)
    while div >=1:
        for i in range(Data.data_count-div):
            frames.append(copy.deepcopy(ds))
            frames[-1][i].set_color('r')
            frames[-1][i+div].set_color('k')

            if ds[i].value>ds[i+div].value:
                ds[i],ds[i+div]=ds[i+div],ds[i]
                frames.append(copy.deepcopy(ds))
                frames[-1][i+div].set_color('r')
                frames[-1][i].set_color('k')

        div=int(div/1.3)

    frames.append(ds)
    return frames