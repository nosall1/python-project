# -*- coding:utf-8 -*-
"""
"""
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import ui
import selenium.webdriver.support.expected_conditions as EC


def yonyou():
    url = 'http://ethcombo.com/home.php'
    driver = webdriver.Chrome()
    driver.get(url)
    driver.maximize_window()
    ui.WebDriverWait(driver, 100).until(EC.visibility_of_element_located((By.NAME, 'wallet')))
    address = driver.find_element_by_name('wallet')
    address.send_keys('0x859f7de035193f5b8af03480cf22baba0cf3fc83')
    start = driver.find_element_by_xpath('/html/body/div[2]/div[1]/form/p[2]/input')
    start.click()
    ui.WebDriverWait(driver, 100).until(EC.visibility_of_element_located((By.ID, 'playFancy')))
    playFancy = driver.find_element_by_id('playFancy')
    playFancy.click()
    while True:
        time.sleep(3)
        playFancy.click()


yonyou()
