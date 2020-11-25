#-*- coding:utf-8 -*-
"""
 分离通道
"""
import cv2
import numpy as np
img=cv2.imread('..\img\lena.jpg')
b,g,r=cv2.split(img)
cv2.imshow('Blue',r)
cv2.imshow('Red',g)
cv2.imshow('Green',b)
cv2.waitKey(0)
cv2.destroyAllWindows()