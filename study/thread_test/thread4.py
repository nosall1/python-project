#-*- coding:utf-8 -*-
"""
"""
import threading
import time
class Counter:# 计数器类
    def __init__(self):
        self.value=0
    def increment(self):
        self.value=self.value+1
        value=self.value
        return value
counter=Counter()

class ThreadDemo(threading.Thread):
    def __init__(self,index,create_time):# 线程构造函数
        threading.Thread.__init__(self)
        self.index=index
        self.create_time=create_time
    def run(self):
        time.sleep(1)
        value=counter.increment()
        print(time.time()-self.create_time,'\t',self.index,'\tvalue',value)


for index in range(100):
    thread=ThreadDemo(index,time.time())
    thread.start()