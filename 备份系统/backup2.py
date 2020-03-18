#-*- coding:utf-8 -*-
#将备份文件生成到日期文件夹
import os
import time

source=['/Users/test/Downloads/code-master']
target_dir='/Users/test/Downloads/'

#日期文件夹
today_dir=target_dir+time.strftime('%Y%m%d')
#时间文件
time_dir=time.strftime('%H%M%S')

touch=today_dir+os.sep+time_dir+'.zip'
command_touch='zip -qr '+touch+' '+' '.join(source)

#逻辑思路判断
#如果文件夹不存在
if os.path.exists(today_dir)==0:
    os.mkdir(today_dir)
if os.system(command_touch)==0:
    print('Success backup UP')
else:
    print('Failed backup')
