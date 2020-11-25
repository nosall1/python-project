#-*- coding:utf-8 -*-
"""
 Createed by xielijiang on 2017/9/8
"""
import cv2
img=cv2.imread('d:\lena.jpg')
cv2.namedWindow('Image')
cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()