#-*- coding:utf-8 -*-
"""
 观察者模式
"""
# #报警器
# class AlarmSensor:
#     def run(self):
#         print 'Alarm Ring...'
# #洒水器
# class WaterSpriker:
#     def run(self):
#         print 'Spray Water...'
# #拨号器
# class EmergencyDialer:
#     def run(self):
#         print 'Dial 119...'
#
# 观察者
class Observer:
    def update(self):
        pass
#报警器
class AlarmSensor(Observer):
    def update(self,action):
        print ('Alarm Got:%s'% action)
        self.runAlarm()
    def runAlarm(self):
        print ('Alarm Ring...')
#洒水器
class WaterSprinker(Observer):
    def update(self,action):
        print ('Sprinker Got:%s'%action)
        self.runSprinker()
    def runSprinker(self):
        print ('Spray Water...')
#拨号器
class EmergencyDialer(Observer):
    def update(self,action):
        print ('Dialer Got:%s'%action)
        self.runDialer()
    def runDialer(self):
        print ('Dial 119...')

# 被观察者
class Observed:
    observers=[]
    action=''
    def addObserver(self,observer):
        self.observers.append(observer)
    def notifyAll(self):
        for obs in self.observers:
            obs.update(self.action)
class smokeSensor(Observed):
    def setAction(self,action):
        self.action=action
    def isFire(self):
        return True

if __name__ == '__main__':
    alarm=AlarmSensor()
    sprinker=WaterSprinker()
    dialer=EmergencyDialer()

    smoker_sensor=smokeSensor()
    smoker_sensor.addObserver(alarm)
    smoker_sensor.addObserver(sprinker)
    smoker_sensor.addObserver(dialer)

    if smoker_sensor.isFire():
        smoker_sensor.setAction('On Fire!')
        smoker_sensor.notifyAll()