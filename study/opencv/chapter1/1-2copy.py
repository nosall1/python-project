#-*- coding:utf-8 -*-
"""
"""
import cv2
import numpy as np

img=cv2.imread('lena.jpg')
#创建新图像
emptyImage=np.zeros(img.shape,np.uint8)
emptyImage2=img.copy()
#获取图像的副本
emptyImage3=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow('EmptyImage',emptyImage)
cv2.imshow('Image',img)
cv2.imshow('EmptyImage2',emptyImage2)
cv2.imshow('EmptyImage3',emptyImage3)
# 对于JPEG，其表示的是图像的质量，用0-100的整数表示，默认为95
cv2.imwrite('cat2.jpg',img,[int(cv2.IMWRITE_JPEG_QUALITY),5])
cv2.imwrite('cat3.jpg',img,[int(cv2.IMWRITE_JPEG_QUALITY),100])
# 对png，第三个参数表示压缩级别，从0到9,压缩级别越高，图像尺寸越小。默认级别为3
cv2.imwrite('cat.png',img,[int(cv2.IMWRITE_PNG_COMPRESSION),0])
cv2.imwrite('cat2.png',img,[int(cv2.IMWRITE_PNG_COMPRESSION),9])
cv2.waitKey(0)
cv2.destroyAllWindows()