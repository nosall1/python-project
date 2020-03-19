#-*- coding:utf-8 -*-

from pymongo import MongoClient
client = MongoClient('mongodb://127.0.0.1:27017')
db = client.school
for student in db.students.find():
    print('学号:', student['stuid'])
    print('姓名:', student['name'])
    print('电话:', student['tel'])

print(db.students.find().count())
print(db.students.remove())
print(db.students.find().count())
