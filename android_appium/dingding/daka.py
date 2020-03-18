# -*- coding:utf-8 -*-
"""
 打卡主程序
"""
import datetime, time

from android_appium.dingding.dingding import dingding

ding = dingding()


def run_Task():
    ding.daka()


def timerFun(sched_Timer):
    flag = 0
    while True:

        now = datetime.datetime.now()
        if now == sched_Timer:
            run_Task()
            time.sleep(1)
            flag = 1
        else:
            if flag == 1:
                sched_Timer = sched_Timer + datetime.timedelta(days=1)
                print(sched_Timer)
                flag = 0


if __name__ == '__main__':
    sched_Timer = datetime.datetime(2018, 1, 5, 10, 30, 50)
    print('run the timer task at {0}'.format(sched_Timer))
    timerFun(sched_Timer)
