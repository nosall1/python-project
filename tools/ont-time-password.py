#-*- coding:utf-8 -*-
# 生成otp
import onetimepass as otp
my_secret = 'LTLBIOUS4S'
my_token = otp.get_totp(my_secret)
print(my_token)