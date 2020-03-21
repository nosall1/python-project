#-*- coding:utf-8 -*-

# 定义默认端口
import os
import re

import tornado.web
from tornado.options import define, parse_command_line, options

define('port',default=8000,type=int)

users={}

# 用户
class User(object):
    def __init__(self,nickname,gender,birthday):
        self.nickname=nickname
        self.gender=gender
        self.birthday=birthday

# 自定义请求处理器
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        # 从cookie中读取用户昵称
        nickname=self.get_cookie('nickname')
        if nickname in users:
            self.render('userinfo.html',user=users[nickname])
        else:
            self.render('userform.html',hint='请填写个人信息')

# 自定义请求处理器
class UserHandle(tornado.web.RequestHandler):
    def post(self):
        # 从表单参数中读取用户昵称，性别和生日信息
        nickname=self.get_body_argument('nickname')
        gender=self.get_body_argument('gender')
        birthday=self.get_body_argument('birthday')
        print(nickname,gender,birthday)
        # 检查用户昵称是否有效
        if not re.fullmatch(r'\w{6,20}',nickname):
            self.render('userform.html',hint='请输入有效的昵称')
        elif nickname in users:
            self.render('userform.html',hint='昵称已经被使用')
        else:
            users[nickname]=User(nickname,gender,birthday)
            # 将用户昵称写入cookie并设置有效期为7天
            a=self.get_cookie('djdt')

            self.set_cookie('nickname',nickname,expires_days=7)
            print(a)
            self.render('userinfo.html',user=users[nickname])

def main():
    parse_command_line()
    app=tornado.web.Application(
        handlers=[
            (r'/',MainHandler),
            (r'/register',UserHandle)
        ],
        template_path=os.path.join(os.path.dirname(__file__),'templates')
    )
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()

if __name__ == '__main__':
    main()