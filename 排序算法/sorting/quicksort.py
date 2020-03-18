#-*- coding:utf-8 -*-
# 快速排序
import copy
from .data import Data
def quick_sort(data_set):
    frames=[data_set]
    ds=copy.deepcopy(data_set)
    qsort(ds,0,Data.data_count,frames)
    frames.append(ds)
    return frames
def qsort(ds,head,tail,frames):
    if tail-head>1:
        ds_y=copy.deepcopy(ds)
        for i in range(head,tail):
            ds_y[i].set_color('y')
        i=head
        j=tail-1
        pivot=ds[j].value
        while i <j :
            frames.append(copy.deepcopy(ds_y))
            frames[-1][i if ds[i].value==pivot else j].set_color('r')
            frames[-1][j if ds[i].value==pivot else i].set_color('k')
            if ds[i].vaule>pivot or ds[j].vaule<pivot:
                ds[i],ds[j]=ds[j],ds[i]
                ds_y[i],ds_y[j]=ds_y[j],ds_y[i]
                frames.append(copy.deepcopy(ds_y))
                frames[-1][i if ds[i].value==pivot else j].set_color('r')
                frames[-1][j if ds[i].value==pivot else i].set_color('k')
            if ds[i].value==pivot:
                j-=1
            else:
                i+=1

        qsort(ds,head,i,frames)
        qsort(ds,i+1,tail,frames)