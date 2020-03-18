#-*- coding:utf-8 -*-


# 冒泡排序
import copy
from .data import Data


def bubble_sort(data_set):
    frames=[data_set]
    ds=copy.deepcopy(data_set)
    for i in range(Data.data_count-1):
        flag=False
        for j in range(Data.data_count-i-1):
            if ds[j].value>ds[j+1].value:
                ds[j],ds[j+1]=ds[j+1],ds[j]
                flag=True

            frames.append(copy.deepcopy(ds))
            frames[-1][j+1].set_color('r')
        if not flag:
            break

    frames.append(ds)
    return frames