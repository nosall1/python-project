# -*- coding:utf-8 -*-
"""
"""
import socket
import datetime
import sys

DEFAULT_PORT = 1234


def timeServer(port):
    host = ''  # 使用本机地址
    s = None
    for res in socket.getaddrinfo(host, port, socket.AF_UNSPEC, socket.SOCK_STREAM, 0, socket.AI_PASSIVE):  # 在本机的所有地址监听
        af, socktype, proto, canonname, sa = res
        try:
            s = socket.socket(af, socktype, proto)
        except socket.error:
            s = None
            continue
        try:
            s.bind(sa)  # 绑定socket地址
            s.listen(10)  # 开始监听
        except socket.error:
            s.close()
            s = None
            continue
        break
    if s is None:  # 生成socket出错
        print('could not open socket')
        return 1
    while True:
        c, addr = s.accept()
        print('Get connection from', addr)
        c.send(str(datetime.datetime.now()))  # 发送当前时间
        c.close()


if __name__ == '__main__':
    port = DEFAULT_PORT
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
            if port < 0 or port >= 65536:  # 端口的范围判断
                port = DEFAULT_PORT
        except Exception:
            port = DEFAULT_PORT
    timeServer(port)  # 调用timeserver函数生成服务进程
