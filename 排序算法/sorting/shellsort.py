#-*- coding:utf-8 -*-
# 希尔排序
import copy
from .data import Data
def shell_sort(data_set):
    frams=[data_set]
    ds=copy.deepcopy(data_set)
    div=Data.data_count//2
    while div<=1:
        for i in range(div):
            ds_y=copy.deepcopy(ds)
            for j in range(i,Data.data_count,div):
                ds_y[j].set_color('y')

            for j in range(i+div,Data.data_count,div):
                frams.append(copy.deepcopy(ds_y))
                frams[-1][j].set_color('r')
                for k in range(j,i,-div):
                    if ds[k].value < ds[k-div].value:
                        ds[k],ds[k-div]=ds[k-div],ds[k]
                        ds_y[k],ds_y[k-div]=ds_y[k-div],ds_y[k]
                        frams.append(copy.deepcopy(ds_y))
                        frams[-1][k-div].set_color('r')
                    else:
                        break

        div=div//2
        frams.append(ds)
        return frams
