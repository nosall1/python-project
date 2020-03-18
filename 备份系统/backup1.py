#-*- coding:utf-8 -*-
import os
import time
# 直接生成备份文件

# 需要备份的目录
source=['/Users/test/Downloads/code-master']
# 生成zip的目录
target_dir='/Users/test/Downloads/'

# 生成的文件
target=target_dir+time.strftime('%Y%m%d%H%M%S')+'.zip'

zip_commond='zip -qr %s %s' %(target,''.join(source))

if os.system(zip_commond)==0:
    print("Successful backup")
else:
    print('Backup Failed')
