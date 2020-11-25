# -*- coding:utf-8 -*-
"""
"""
import cv2
import numpy

img = cv2.imread('..\img\\building.jpg', 0)

# 构造一个3x3的结构元素
element = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
dilate = cv2.dilate(img, element)
erode = cv2.erode(img, element)

# 将两幅图像相见获得边，第一个参数是膨胀后的图像，第二个参数是腐蚀后的图像
result = cv2.absdiff(dilate, erode)

# 上面得到的结果是灰度图,将其二值化以便更清楚的观察结果
retval, result = cv2.threshold(result, 40, 255, cv2.THRESH_BINARY)
# 反色，即对二值图每个像素取反
result = cv2.bitwise_not(result)
# 显示图像
cv2.imshow('result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
