#-*- coding:utf-8 -*-
"""
 使用Numpy分离
"""
import cv2
import numpy as np
img=cv2.imread('..\img\lena.jpg')
b=np.zeros((img.shape[0],img.shape[1]),dtype=img.dtype)
g=np.zeros((img.shape[0],img.shape[1]),dtype=img.dtype)
r=np.zeros((img.shape[0],img.shape[1]),dtype=img.dtype)
b[:,:]=img[:,:,0]
g[:,:]=img[:,:,1]
r[:,:]=img[:,:,2]

#合并
merged=cv2.merge([b,g,r])
print('Merge by opencv')
print( merged.strides)
print(merged)

mergedByNp=np.dstack([b,g,r])
print ('Merge by Numpy')
print (mergedByNp.strides)
print (mergedByNp)


cv2.imshow('Merged',merged)
cv2.imshow('MergedByNp',mergedByNp)
cv2.imshow("Blue",r)
cv2.imshow('Red',g)
cv2.imshow('Green',b)
cv2.waitKey(0)
cv2.destroyAllWindows()