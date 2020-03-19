#-*- coding:utf-8 -*-
import redis

client=redis.Redis(host='127.0.0.1',port=6379,password='yourpass')
print(client.set('usrenmae','admin'))
print(client.hset('student','name','hao'))
print(client.hset('student','age',38))
print(client.keys('*'))
print(client.get('username'))
print(client.hgetall('student'))