#-*- coding:utf-8 -*-
import heapq

list1 = [34, 25, 12, 99, 87, 63, 58, 78, 88, 92]
list2 = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]
# 输出list1中最大的3个数
print(heapq.nlargest(3,list1))
# 输出list1中最小的3个数
print(heapq.nsmallest(3,list1))
# 输出list2中按照price排序，最大的两个数据
print(heapq.nlargest(2,list2,key=lambda x:x['price']))
# 输出list2中按照shares排序，最小的两个数据
print(heapq.nsmallest(2,list2,key=lambda x:x['shares']))