# -*- coding:utf-8 -*-
"""
 门面模式
"""


# 火灾报警系统
# 一个警报器
class AlarmSensor:
    def run(self):
        print ('Alarm Ring...')


# 一个喷水器
class WaterSprinker:
    def run(self):
        print ('Spray Water ...')


# 一个自动拨打电话的装置
class EmergencyDialer:
    def run(self):
        print ('Dial 119...')


class EmergencyFacade:
    def __init__(self):
        self.alarm_sensor = AlarmSensor()
        self.water_sprinker = WaterSprinker()
        self.emergency_dialer = EmergencyDialer()

    def runAll(self):
        self.alarm_sensor.run()
        self.water_sprinker.run()
        self.emergency_dialer.run()


if __name__ == '__main__':
    emergency_facade = EmergencyFacade()
    emergency_facade.runAll()
