#-*- coding:utf-8 -*-
"""
"""
import threading
import random,time
class ThreadLocal():
    def __init__(self):
        self.local=threading.local() # 生成local数据对象

    def run(self):
        time.sleep(random.random())
        self.local.number=[]
        for i in range(10):
            self.local.number.append(random.choice(range(10)))
        print(threading.current_thread(),self.local.number)

threadLocal=ThreadLocal()
threads=[]
for i in range(5):
    t =threading.Thread(target=threadLocal.run)
    t.start()# 启动线程
    threads.append(t)

for i in range(5):
    threads[i].join()