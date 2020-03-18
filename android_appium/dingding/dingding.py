# -*- coding:utf-8 -*-
import time

import os

from appium import webdriver


class dingding():
    def get_size(self, driver):
        x = driver.get_window_size()['width']
        y = driver.get_window_size()['height']
        return (x, y)

    # 向上滑动
    def swipe_up(self, driver, t):
        l = self.get_size(driver)
        x1 = int(l[0] * 0.5)  # x坐标
        y1 = int(l[1] * 0.75)  # 起点y坐标
        y2 = int(l[1] * 0.25)  # 终点y坐标
        driver.swipe(x1, y1, x1, y2, t)

    # 退出登录
    def log_out(self, driver):
        # 找到设置
        set_ting = driver.find_element_by_id('com.alibaba.android.rimet:id/rl_setting')
        set_ting.click()
        # 向上滑动
        self.swipe_up(driver, 1000)
        logout = driver.find_element_by_name(u'退出登录')
        logout.click()
        ok_button = driver.find_element_by_id('android:id/button1')
        ok_button.click()

    # 获取“工作”
    def get_work(self, driver):
        work_table = driver.find_element_by_name(u'工作')
        work_table.click()

    # 获取“我的”
    def get_mime(self, driver):
        # 获取最后一个
        tables = driver.find_elements_by_class_name('android.widget.RelativeLayout')
        tables[-1].click()
        time.sleep(3)
        self.swipe_up(driver, 1500)

    def daka(self):

        # 点亮屏幕
        os.system('adb shell input keyevent 26')
        # 向上滑动
        os.system('adb shell input swipe 530 1680 530 1000')
        PATH = lambda p: os.path.abspath(
            os.path.join(os.path.dirname(__file__), p)
        )

        desired_caps = {}
        desired_caps['deviceName'] = 'cda7f417'

        # desired_caps['deviceName'] = 'XPUDU17214021705'
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0.1'
        # desired_caps['platformVersion'] = '7.0'
        desired_caps['app'] = PATH('./rimet_10002068.apk')
        desired_caps['appPackage'] = 'com.alibaba.android.rimet'
        # 在真机上必须是从主页面调用，不能直接调用其他activity
        desired_caps['appActivity'] = 'com.alibaba.android.rimet.biz.SplashActivity'
        # desired_caps['unicodeKeyboard'] = True
        # desired_caps['resetKeyboard'] = True
        # desired_caps['appPackage'] = 'com.zcbl.bjjj_driving'
        # desired_caps['appActivity'] = 'com.zcbl.driving_simple.activity.FirstPagerAcitivty'
        driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        time.sleep(2)

        # 点击登录按钮
        login_button = driver.find_element_by_name(u'登录')
        login_button.click()

        # # 获取登录按钮
        texts = driver.find_elements_by_class_name('android.widget.EditText')
        # 输入用户名
        texts[0].clear()
        texts[0].send_keys('***')
        # 输入密码
        texts[1].clear()
        texts[1].send_keys('***')
        time.sleep(2)
        # 点击登录
        login = driver.find_element_by_class_name('android.widget.Button')
        login.click()
        print('登录成功')
        time.sleep(3)

        # 获取工作
        self.get_work(driver)
        # 点击“考勤打卡”
        driver.tap([(145, 1015)])
        print('进入考勤打开')
        time.sleep(3)
        # 点击“打卡”
        driver.tap([(530, 1200)])
        print('打卡')
        time.sleep(5)
        # 点击返回
        back = driver.find_element_by_id('com.alibaba.android.rimet:id/back_icon')
        back.click()

        # 点击"我的"
        self.get_mime(driver)
        time.sleep(3)
        # 向上滑动
        self.swipe_up(driver, 1000)
        # 点击设置
        setting = driver.find_element_by_name(u'设置')
        print('进入设置')
        setting.click()
        time.sleep(3)
        # 点击退出登录
        login_out = driver.find_element_by_name(u'退出登录')
        print('退出登录')
        login_out.click()
        time.sleep(3)
        ok_button = driver.find_element_by_name(u'确认')
        ok_button.click()
