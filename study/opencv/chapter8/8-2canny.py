#-*- coding:utf-8 -*-
"""
"""

import cv2

def CannyThreshole(lowThreshold):
    detected_edges=cv2.GaussianBlur(gray,(3,3),0)
    detected_edges=cv2.Canny(detected_edges,lowThreshold,lowThreshold*ratio,apertureSize=kernel_size)
    dst=cv2.bitwise_and(img,img,mask=detected_edges)
    cv2.imshow('canny demo',dst)

lowThreshold=0
max_lowThreshlod=100
ratio=3
kernel_size=3
img=cv2.imread('..\img\lion.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.namedWindow('canny demo')
cv2.createTrackbar('Min threshold','canny demo',lowThreshold,max_lowThreshlod,CannyThreshole)
CannyThreshole(0)

if cv2.waitKey(0)==27:
    cv2.destroyAllWindows()