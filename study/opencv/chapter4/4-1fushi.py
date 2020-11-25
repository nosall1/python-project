#-*- coding:utf-8 -*-
"""
 腐蚀图像
"""
import cv2
import numpy as np

img=cv2.imread('..\img\lena.jpg',0)

#opencv定义的结构元素
kernel=cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))

#腐蚀图像
eroded=cv2.erode(img,kernel)
#显示腐蚀后的图像
cv2.imshow('Eroded image',eroded)

#膨胀图像
dilated=cv2.dilate(img,kernel)
#显示膨胀后的图像
cv2.imshow('Dilated image',dilated)
#原图像
cv2.imshow('Origin',img)


#Numpy定义的结构元素
NpKernel=np.uint8(np.ones((3,3)))
NPeroded=cv2.erode(img,NpKernel)
#显示腐蚀后的图像
cv2.imshow('Eroded by Numpy kernel',NPeroded)

cv2.waitKey(0)
cv2.destroyAllWindows()