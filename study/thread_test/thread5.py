# -*- coding:utf-8 -*-
"""
"""
import threading

from study.thread_test.thread1 import thread


class Counter:
    def __init__(self):
        self.value = 0
        self.lock = thread.allocate_lock()


def increment(self):
    self.lock.acquire()  # 获取锁，进入临界区
    self.value = self.value + 1
    value = self.value
    self.lock.release()  # 释放锁，离开临界区
    return value
# 高层次threading 锁机制版本
class Counter:
    def __init__(self):
        def __init__(self):
            self.value = 0
            self.lock = threading.Lock()
def increment(self):
    self.lock.acquire()  # 获取锁，进入临界区
    self.value = self.value + 1
    value = self.value
    self.lock.release()  # 释放锁，离开临界区
    return value