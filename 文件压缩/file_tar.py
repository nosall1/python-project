#-*- coding:utf-8 -*-
"""
 文档归档
"""
import tarfile
tar=tarfile.open('textfile.tar','w')
# tar=tarfile.open('large.tar.gz','w:gz') # 打gz包
tar.add('1.txt')
tar.add('2.txt')
tar.add('3.txt')
tar.close()

# 获取tar文件中的所有文件名
tar.getnames()
# 获取所有文件
tar.list()
# 将压缩包解压到tmp目录下
tar.extractall('tmp')