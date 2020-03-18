#-*- coding:utf-8 -*-
# 客户端程序
import json
from base64 import b64decode
from socket import socket


def main():
    client=socket()
    client.connect(('',5555))
    # 定义一个保存二进制数据的对象
    in_data=bytes()
    # 由于不知道服务器发送的数据有多大，每次接收1024字节
    data=client.recv(1024)
    while data:
        # 将接收的数据拼接起来
        in_data+=data
        data=client.recv(1024)

    # 将接收的二进制数据解码成json字符串并转换为字典
    # loads 函数的作用就是将json字符串转成字典对象
    my_dict=json.loads(in_data.decode('utf-8'))
    filename=my_dict['filename']
    filedata=my_dict['filedata'].encode('utf-8')
    with open('test.jpg','wb') as f:
        # 将base64格式的数据解码成二进制数据并写入文件
        f.write(b64decode(filedata))

    print('图片已经保存')

if __name__ == '__main__':
    main()