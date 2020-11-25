# -*- coding:utf-8 -*-
"""
"""
import time
from socketserver import ForkingMixIn, TCPServer, StreamRequestHandler


class Server(ForkingMixIn, TCPServer):
    pass


class MyHandler(StreamRequestHandler):
    def handle(self):
        addr = self.request.getpeername()
        print('Get connection from', addr)  # 打印客户端地址
        time.sleep(5)
        self.wfile.write('This is a ForkingMixIn tcp socket server')  # 发送信息


host = ''
port = 1234
server = Server((host, port), MyHandler)
server.serve_forever()  # 开始侦听并处理连接
