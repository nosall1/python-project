#-*- coding:utf-8 -*-
"""
 开运算和闭运算
"""
import cv2
import numpy as np
img=cv2.imread('..\img\lena.jpg',0)
#定义结构元素

kernel=cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))

#闭运算
closed=cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel)
#显示腐蚀后的图像
cv2.imshow('Close',closed)

#开运算
opened=cv2.morphologyEx(img,cv2.MORPH_OPEN,kernel)
#显示腐蚀后的图像
cv2.imshow('open',opened)

cv2.waitKey(0)
cv2.destroyAllWindows()