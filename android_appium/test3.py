# -*- coding:utf-8 -*-
"""
 从定位软件打开钉钉
"""
import os

import time
from appium import webdriver


def get_size(driver):
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    return (x, y)


# 向上滑动
def swipe_up(driver, t):
    l = get_size(driver)
    x1 = int(l[0] * 0.5)  # x坐标
    y1 = int(l[1] * 0.75)  # 起点y坐标
    y2 = int(l[1] * 0.25)  # 终点y坐标
    driver.swipe(x1, y1, x1, y2, t)


# 退出登录
def log_out(driver):
    # 找到设置
    set_ting = driver.find_element_by_id('com.alibaba.android.rimet:id/rl_setting')
    set_ting.click()
    # 向上滑动
    swipe_up(driver, 1000)
    logout = driver.find_element_by_name(u'退出登录')
    logout.click()
    ok_button = driver.find_element_by_id('android:id/button1')
    ok_button.click()

# 获取“工作”
def get_work(driver):
    work_table=driver.find_element_by_name('com.alibaba.android.rimet:id/home_bottom_tab_text')
    work_table.click()



# 获取“我的”
def get_mime(driver):
    # 获取最后一个
    tables = driver.find_elements_by_class_name('android.widget.RelativeLayout')
    tables[-1].click()
    time.sleep(3)
    swipe_up(driver, 1500)




PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)

desired_caps = {}
desired_caps['deviceName'] = 'Custom5.1.0'
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '4.4.2'
# desired_caps['app'] = PATH('./rimet_10002068.apk')
desired_caps['appPackage'] = 'io.xndwofxndwZS'
desired_caps['appActivity'] = 'io.xndwofxndwZS.home.MapActivity'

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

time.sleep(2)
weizhi = driver.find_element_by_id('io.xndwofxndwZS:id/lin_baoguo')
weizhi.click()
time.sleep(1)
qianwang = driver.find_element_by_name(u'前往')
qianwang.click()
time.sleep(1)
# 打开钉钉
open_dingding = driver.find_element_by_id('io.xndwofxndwZS:id/bt_goDD')
open_dingding.click()
time.sleep(5)

# 登录钉钉
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
time.sleep(3)

# 获取工作
get_work(driver)
driver.tap([100,100])
