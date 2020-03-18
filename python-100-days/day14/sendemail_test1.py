#-*- coding:utf-8 -*-

# 简单发送邮件
from email.header import Header
from email.mime.text import MIMEText
from smtplib import SMTP


def main():
    sender='test1@126.com'
    receivers=['test2@163.com','test3@163.com']
    message=MIMEText('用Python发送邮件','plain','utf-8')
    message['From']=Header('张三','utf-8')
    message['To']=Header('里斯','utf-8')
    message['Subject']=Header('示例代码实验邮件','utf-8')
    smtper=SMTP('smtp.126.com')
    smtper.login(sender,'11111')
    smtper.sendmail(sender,receivers,message.as_string())
    print('邮件发送完成')

if __name__ == '__main__':
    main()