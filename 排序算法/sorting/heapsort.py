#-*- coding:utf-8 -*-
import copy
from .data import Data
# 堆排序
def heap_sort(data_set):
    frames=[data_set]
    ds=copy.deepcopy(data_set)
    for i in range(Data.data_count//2-1,-1,-1):
        heap_adjust(ds,i,Data.data_count,frames)
    for i in range(Data.data_count-1,0,-1):
        ds[i],ds[0]=ds[0],ds[i]
        heap_adjust(ds,0,i,frames)

    frames.append(ds)
    return frames

def heap_adjust(ds,head,tail,frames):
    i=head*2+1
    while i<tail:
        if i+1<tail and ds[i].value <ds[i+1].value:
            i+=1

        ds_c=color(ds,tail)
        frames.append(ds_c)
        ds_c[i].set_color('k')
        ds_c[head].set_color('r')

        if ds[i].value<=ds[head].value:
            break

        ds[head],ds[i]=ds[i],ds[head]

        ds_c=copy.deepcopy(ds_c)
        frames.append(ds_c)
        ds_c[head],ds_c[i]=ds_c[i],ds_c[head]

        head=i
        i=i*2+1

def color(ds,n):
    ds_c=copy.deepcopy(ds)
    head=0
    tail=1
    count=1
    depth=0
    colors='bmgcy'
    while head<n:
        for i in range(head,min(tail,n)):
            ds_c[i].set_color(colors[depth%len(colors)])
        head=tail
        count*=2
        tail+=count
        depth+=1

    return ds_c
