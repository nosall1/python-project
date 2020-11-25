#-*- coding:utf-8 -*-
"""
 Createed by xlj on 2018/2/26
 线性相关矩阵秩计算样例
"""
import numpy as np
# 初始化一个2x2的线性相关矩阵
M=np.array([[1,2],[2,4]])

# 计算2x2线性相关矩阵的秩
print (np.linalg.matrix_rank(M,tol=None))