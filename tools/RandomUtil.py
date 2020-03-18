# -*- coding: utf-8 -*-
# 随机数生成

import codecs
import json
import random


#生成随机字母

import requests


#随机生成字母和数字的组合
def getRndStrByLen(num):
    code_list = []
    for i in range(10): # 0-9数字
        code_list.append(str(i))
    for i in range(65, 91): # A-Z
        code_list.append(chr(i))
    myslice = random.sample(code_list, num)  # 从list中随机获取6个元素，作为一个片断返回
    verification_code = ''.join(myslice) # list to string
    return verification_code


#生成随机数字
def getRndNumByLen(num):
    ''' 随机生成6位的验证码 '''
    code_list = []
    for i in range(10): # 0-9数字
        code_list.append(str(i))

    n_list=[]
    for i in range(num):
        myslice = random.choice(code_list)  # 从list中随机获取6个元素，作为一个片断返回
        n_list.append(myslice)
    code="".join(n_list)
    return code


#随机生成纯字母
def getRndStrSByLen(num):
    code_list = []
    # for i in range(10): # 0-9数字
    #     code_list.append(str(i))
    for i in range(65, 91): # A-Z
        code_list.append(chr(i))
    for i in range(65, 91): # A-Z
        code_list.append(chr(i))
    for i in range(97, 122): # a-z
        code_list.append(chr(i))
    myslice = random.sample(code_list, num)  # 从list中随机获取6个元素，作为一个片断返回
    verification_code = ''.join(myslice) # list to string
    return verification_code






