#-*- coding:utf-8 -*-
# 猴子排序
import copy
import random
from .data import Data

def monkey_sort(data_set,frame_count):
    frames=[data_set]
    dataes=[data.value for data in data_set]
    flag=False
    while not flag:
        flag=True
        for i in range(Data.data_count-1):
            ds=[Data(d) for d in dataes]
            frames.append(ds)
            ds[i].set_color('r')
            ds[i+1].set_color('k')
            if len(frames)==frame_count:
                return frames
            if dataes[i] > dataes[i+1]:
                flag=False
                break
        if not flag:
            random.shuffle(dataes)

    frames.append(Data(d) for d in dataes)
    return frames