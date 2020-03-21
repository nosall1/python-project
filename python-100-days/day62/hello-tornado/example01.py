#-*- coding:utf-8 -*-
import tornado.ioloop
import tornado.web
from tornado.options import define, parse_command_line, options

# 定义端口
define('port',default=8000,type=int)

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('<h1>hello world</h1>')

def main():
    parse_command_line()
    app=tornado.web.Application(handlers=[(r'/',MainHandler)])
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()

if __name__ == '__main__':
    main()