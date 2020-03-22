#-*- coding:utf-8 -*-
# 聊天服务器
import os

import tornado.web
from handlers import LoginHandler,ChatHandler
if __name__ == '__main__':
    app=tornado.web.Application(
        handlers=[
            (r'/login',LoginHandler),
            (r'/chat',ChatHandler)
        ],
        template_path=os.path.join(os.path.dirname(__file__), 'templates'),
        static_path=os.path.join(os.path.dirname(__file__), 'static'),
        cookie_secret='MWM2MzEyOWFlOWRiOWM2MGMzZThhYTk0ZDNlMDA0OTU='
    )
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
