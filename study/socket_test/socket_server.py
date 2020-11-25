#-*- coding:utf-8 -*-
"""
"""
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM) # 生成socket对象
host=socket.gethostname()
port=1234
s.bind((host,port)) # 绑定socket地址
s.listen(10) #开始监听
while True:
    c,addr=s.accept() # 接受一个连接
    print('Get connection from',addr)
    c.send('This is a simple server') # 发送数据
    c.close()