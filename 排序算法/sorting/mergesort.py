#-*- coding:utf-8 -*-
import copy
from .data import Data
# 归并排序
def merge_sort(data_set):
    frames=[data_set]
    ds=copy.deepcopy(data_set)
    split_merge(ds,0,Data.data_count,frames)
    frames.append(ds)
    return frames
def split_merge(ds,head,tail,frames):
    mid=(head+tail)//2
    if tail-head>2:
        split_merge(ds,head,mid,frames)
        split_merge(ds,mid,tail,frames)

    ds_yb=copy.deepcopy(ds)
    for i in range(head,mid):
        ds_yb[i].set_color('y')
    for i in range(mid,tail):
        ds_yb[i].set_color('b')

    left=head
    right=mid

    tmp_list=[]
    for i in range(head,tail):
        frames.append(copy.deepcopy(ds_yb))
        if right==tail or (left<mid and ds[left].value <=ds[right].value):
            tmp_list.append(ds[left])
            frames[-1][left].set_color('r')
            left+=1
        else:
            tmp_list.append(ds[right])
            frames[-1][right].set_color('r')
            right+=1

    for i in range(head,tail):
        ds[i]=tmp_list[i-head]

    frames.append(copy.deepcopy(ds))
