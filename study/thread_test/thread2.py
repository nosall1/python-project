#-*- coding:utf-8 -*-
"""
"""
import threading

import time


class ThreadDemo(threading.Thread):
    def __init__(self,index,create_time):# 线程构造函数
        threading.Thread.__init__(self)
        self.index=index
        self.create_time=create_time
    def run(self):# 具体的线程运行代码
        time.sleep(1)# 休眠1秒
        print(time.time()-self.create_time),'\t',self.index
        print("Thread %d exit ..."% (self.index))
threads=[]
for index in range(5):
    thread=ThreadDemo(index,time.time())
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()
print('Main thread exit...')
