#-*- coding:utf-8 -*-
"""
 检测拐角
"""
import cv2

img = cv2.imread('..\img\\building.jpg', 0)
origin=cv2.imread('..\img\\building.jpg')
#构造5x5的结构元素，分别为十字形，菱形，
cross=cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))
#菱形结构元素的定义稍麻烦一些
diamond=cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
diamond[0,0]=0
diamond[0,1]=0
diamond[1,0]=0
diamond[4,4]=0
diamond[4,3]=0
diamond[3,4]=0
diamond[4,0]=0
diamond[4,1]=0
diamond[3,0]=0
diamond[0,3]=0
diamond[0,4]=0
diamond[1,4]=0
#方形
square=cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
#x型
x=cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))

#使用cross膨胀图像
result1=cv2.dilate(img,cross)
#使用菱形腐蚀图像
result1=cv2.erode(result1,diamond)

#使用x膨胀原图像
result2=cv2.dilate(img,x)
#使用方形腐蚀图像
result2=cv2.erode(result2,square)

#将两幅闭运算图像相减获得角
result=cv2.absdiff(result2,result1)
#使用阈值获得二值图
retval,result=cv2.threshold(result,40,255,cv2.THRESH_BINARY)

#在原图上用半径为5的圆圈将点标出
for j in range(result.size):
    y=j/result.shape[0]
    x=j%result.shape[0]

    if result[x,y]==255:
        cv2.circle(img,(y,x),5,(255,0,0))

# # 反色，即对二值图每个像素取反
# result = cv2.bitwise_not(result)
cv2.imshow('Result',result)
cv2.waitKey(0)
cv2.destroyAllWindows()