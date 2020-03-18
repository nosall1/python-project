#-*- coding:utf-8 -*-
import json
# json数据格式化

def jsonformat(r):
    return json.dumps(r,sort_keys=True,indent=2,ensure_ascii=False)