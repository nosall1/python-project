#-*- coding:utf-8 -*-
"""
"""
import numpy as np
import cv2
# import matplotlib.pyplot as plt

img=np.array([
    [[255,0,0],[0,255,0],[0,0,255]],
    [[255,255,0],[255,0,255],[0,255,255]],
    [[255,255,255],[128,128,128],[0,0,0]],
],dtype=np.uint8)

# # 用matpltlib存储
# plt.imsave('img_pyplot.jpg',img)

# 用opencv存储
cv2.imwrite('img_cv2.jpg',img)