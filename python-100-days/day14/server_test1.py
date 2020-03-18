#-*- coding:utf-8 -*-
# 服务端程序
import json
from base64 import b64encode
from socket import socket
from threading import Thread

def main():
    # 自定义线程类
    class FileTransferHandler(Thread):
        def __init__(self,cclient):
            super().__init__()
            self.cclient=cclient
        def run(self):
            my_dict={}
            my_dict['filename']='guido.jpg'
            # JSON是纯文本不能携带二进制数据
            # 所以图片的二进制数据要处理成base64编码
            my_dict['filedata']=data
            print(data)
            # 通过dumps函数将字典处理成JOSN字符串
            json_str=json.dumps(my_dict)
            # 发送json字符串
            self.cclient.send(json_str.encode('utf-8'))
            self.cclient.close()

    # 创建套接字对象并指定使用哪种传输服务
    server=socket()
    # 绑定IP地址和端口
    server.bind(('',5555))
    # 开启监听
    server.listen(512)

    with open('guido.jpg','rb') as f:
        # 将二进制数据处理成bae64再解码成字符串
        data=b64encode(f.read()).decode('utf-8')

    while True:
        client,addr=server.accept()
        # 启动一个线程来处理客户端请求
        FileTransferHandler(client).start()

if __name__ == '__main__':
    main()