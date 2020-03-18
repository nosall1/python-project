# -*- coding:utf-8 -*-
"""
发送邮件
"""
import smtplib
# sender是邮件发送人邮箱，passwd是服务器授权码，mail_host是服务器地址（这里是QQsmtp服务器）
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

sender = 'test1@qq.com'
password = 'dfsfqwer'
mail_host = 'smtp.qq.com'

# receivers是邮件接收人，用列表保存，可以添加多个
receivers = ['test1@163.com', 'test2@163.com']
# 设置email信息
msg = MIMEMultipart()
# 邮件主题
msg['Subject'] = u'主题'
# 发送方信息
msg['From'] = sender
# 邮件正文是MIMEText:
msg_content = 'text'
msg.attach(MIMEText(msg_content, 'plain', 'utf-8'))
# 添加附件就是加上一个MIMEBase，从本地读取一个突破
with open(u'e://1.png', 'rb') as f:
    # 设置附件的MIME和文件名，这里是jpg类型，可以换png或其他类型：
    mime = MIMEBase('image', 'png', filename='Lyon.png')
    # 加上必要的头信息：
    mime.add_header('Content-Disposition', 'attachment', filename='Lyon.png')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # 把附件的内容读进来
    mime.set_payload(f.read())
    # 用base64编码：
    encoders.encode_base64(mime)
    # 添加到MIMEMultipart:
    msg.attach(mime)

# 登录并发送邮件
try:
    # QQstmp服务器的端口号为465或587
    s = smtplib.SMTP_SSL('smtp.qq.com', 465)
    s.set_debuglevel(1)
    s.login(sender, password)
    # 给receivers列表中的联系人逐个发送邮件
    for item in receivers:
        msg['To'] = to = item
        s.sendmail(sender, to, msg.as_string())
        print ('Success')
    s.quit()
    print ('All emials have been send over')
except smtplib.SMTPException as e:
    print ('Failed,%s', e)
