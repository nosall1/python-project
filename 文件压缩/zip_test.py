#-*- coding:utf-8 -*-

'''
将文件夹压缩为zip
'''

import os
import zipfile

# 创建压缩文件
def create_zip(path):
    zip_file=zipfile.ZipFile(os.path.basename(path)+".zip",'w')
    print("开始压缩文件")
    for root,dirs,files in os.walk(path,topdown=False):
        for name in dirs:
            print("正在压缩文件夹："+os.path.join(root,name))
            zip_file.write(os.path.join(root,name))

        for name in files:
            print("正在压缩文件："+os.path.join(root,name))
            zip_file.write(os.path.join(root,name))
# 解压文件
def uncompress_zip(path):
    print('正在解压文件...')
    zfile=zipfile.ZipFile(path,'r')
    zfile.extractall()


if __name__ == '__main__':
    path_info='test1.zip'
    if os.path.isdir(path_info):
        create_zip(path_info)
        print("压缩完成")
    elif os.path.isfile(path_info):
        uncompress_zip(path_info)
        print("解压完成")
    else:
        print("文件类型错误，请重试")