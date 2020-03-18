# -*- coding:utf-8 -*-


# 功能: 爬取新浪微博用户的信息
# 信息：用户ID 用户名 粉丝数 关注数 微博数 微博内容
import codecs

import time

import re
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
import selenium.webdriver.support.ui as ui

# 先调用无界面浏览器PhantomJS
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
wait = ui.WebDriverWait(driver, 10)


# 全局变量，文件操作读写信息
# inforead=codecs.open('SinaWeibo_List.txt','r','utf-8')
# infofile=codecs.open('SinaWeibo_Info.txt','w','utf-8')
# 存储用户相应信息，user_i


def scroll(driver):
    driver.execute_script("""
        (function () {
            var y = document.body.scrollTop;
            var step = 100;
            window.scroll(0, y);


            function f() {
                if (y < document.body.scrollHeight) {
                    y += step;
                    window.scroll(0, y);
                    setTimeout(f, 50);
                }
                else {
                    window.scroll(0, y);
                    document.title += "scroll-done";
                }
            }


            setTimeout(f, 1000);
        })();
        """)


# ********************************************************************************
#                  第一步: 登陆weibo.cn 获取新浪微博的cookie
#        该方法针对weibo.cn有效(明文形式传输数据) weibo.com见学弟设置POST和Header方法
#                LoginWeibo(username, password) 参数用户名 密码
#                             验证码暂停时间手动输入
# ********************************************************************************

def LoginWeibo(username, password):
    try:

        # **********************************************************************
        # 直接访问driver.get("http://weibo.cn/515436")会跳转到登陆页面 用户id
        #
        # 用户名<input name="mobile" size="30" value="" type="text"></input>
        # 密码 "password_4903" 中数字会变动,故采用绝对路径方法,否则不能定位到元素
        #
        # 勾选记住登录状态check默认是保留 故注释掉该代码 不保留Cookie 则'expiry'=None
        # **********************************************************************

        # 输入用户名/密码登录
        print('准备登录Weibo.cn网站...')
        driver.get('http://weibo.com/')
        # time.sleep(5)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'loginname')))
        elem_user = driver.find_element_by_id('loginname')
        elem_user.send_keys(username)
        elem_pwd = driver.find_element_by_name('password')
        elem_pwd.send_keys(password)
        elem_sub = driver.find_element_by_xpath(".//*[@id='pl_login_form']/div/div[3]/div[6]/a")
        elem_sub.click()
        # 获取coockie
        print(driver.current_url)
        # print(driver.get_cookies())  # 获得cookie信息,dict存储
        print(u'输出Cookie值对信息：')
        for cookie in driver.get_cookies():
            for key in cookie:
                print(key, cookie[key])

        print('登陆成功')
    except Exception as e:
        print("Error:", e)
    finally:
        print("End LoginWeibo!\n")


def VisitPersonPage(user_id):

    userfile = codecs.open('weibo-%s.txt' % user_id, 'w', 'utf-8')
    try:
        # global infofile
        print(u'准备访问个人网站...')
        driver.get('http://weibo.com/' + user_id)
        # 用户id
        print('个人详细信息')
        print('***********************')
        print('用户id:' + str(user_id))

        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 'username')))
        # 昵称
        str_name = driver.find_element_by_class_name('username')
        str_t = str_name.text.split(" ")
        num_name = str_t[0]
        # 微博数
        # weibo_num=driver.find_elements_by_class_name('W_f18')
        force = driver.find_element_by_class_name('tb_counter')
        s_lines = force.find_elements_by_class_name('S_line1')
        guanzhu = s_lines[0].text.split('\n')[0]
        fensi = s_lines[1].text.split('\n')[0]
        weibo = s_lines[2].text.split('\n')[0]
        print('关注数：' + str(guanzhu))
        print('粉丝数：' + str(fensi))
        print('微博数：' + str(weibo))

        # ***************************************************************************
        # No.2 文件操作写入信息
        # ***************************************************************************

        userfile.write('===========================================\r\n')
        userfile.write(u'用户: ' + user_id + '\r\n')
        userfile.write(u'昵称: ' + num_name + '\r\n')
        userfile.write(u'微博数: ' + str(guanzhu) + '\r\n')
        userfile.write(u'关注数: ' + str(fensi) + '\r\n')
        userfile.write(u'粉丝数: ' + str(weibo) + '\r\n')
        userfile.write(u'微博内容: ' + '\r\n\r\n')

        # ***************************************************************************
        # No.3 获取微博内容
        # http://weibo.cn/guangxianliuyan?filter=0&page=1
        # 其中filter=0表示全部 =1表示原创
        # ***************************************************************************


        print('\n')
        print('获取微博内容信息')
        num = 1
        while num < 5:
            url_web = 'http://weibo.com/' + user_id + '/home?is_all=1&page=' + str(num)
            print(url_web)
            driver.get(url_web)
            time.sleep(2)
            # 将页面拉倒最底部
            for i in range(5):
                scroll(driver)
                time.sleep(5)
            WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.page.S_txt1')))

            infos = driver.find_elements_by_css_selector('.WB_cardwrap.WB_feed_type.S_bg2 ')
            # infos=driver.find_elements_by_class_name('WB_detail')
            for value in infos:
                print(value.text)
                info = value.text
                if u'转发微博' not in info:
                    print(u'原创微博')
                    userfile.write(u'原创微博\r\n')
                else:
                    print(u'转发微博')
                    userfile.write(u'转发微博\r\n')

                # 获取点赞数
                str1 = info.split(u'ñ')
                if str1:
                    # 获取点赞数
                    val1 = str1[-1]
                    print(u'点赞数：' + val1)
                    userfile.write(u'点赞数：' + val1 + '\r\n')
                    # #获取评论数
                    # val2=str1[0].split('\n')[-2]
                    # print u'评论数：'+val1
                    # userfile.write(u'评论数：'+val1+'\r\n')
                    # #获取转发数
                    # val3=str1[0].split('\n')[-3]
                    # print u'转发数：'+val1
                    # userfile.write(u'转发数：'+val1+'\r\n')

                str2 = info.split(u'û')[-1]

                # 获取收藏数
                str3 = str2.split('\n')[0]
                print('收藏数：' + str3)
                userfile.write(u'收藏数：' + str3 + '\r\n')
                # 获取转发数
                str4 = str2.split('\n')[1]
                print(u'转发数：' + val1)
                userfile.write(u'转发数：' + str4 + '\r\n')
                # 获取评论数
                str5 = str2.split('\n')[2]
                print (u'评论数：' + val1)
                userfile.write(u'评论数：' + str5 + '\r\n')

                print(u'微博内容：')
                str2 = info.split(u'阅读')[0]
                print(str2)
                userfile.write(str2)
                userfile.write('\r\n')
                print('\n\n')
                userfile.write('**********************************************\n')
            num += 1
        print ('**********************************************')

    except Exception as e:
        print("Error: ", e)
    finally:
        print(u'VisitPersonPage!\n\n')
        print('**********************************************\n')


def get_force_user(user_id):
    userfile = codecs.open('User-%s.txt' % user_id, 'w', 'utf-8')
    # 访问个人网站
    driver.get('http://weibo.com/' + user_id)
    # 获取关注数

    try:
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'S_line1')))
        force = driver.find_elements_by_class_name('S_line1')[0]
        a = force.find_element_by_tag_name('a')
        # 点击关注，进入关注页面
        sta = driver.find_element_by_tag_name('strong')
        sta.click()
        # a.click()
        # time.sleep(5)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.W_f14.S_txt1')))
        # 获取关注用户列表
        # user_list1=driver.find_elements_by_class_name('mod_info')

        user_list = []

        time.sleep(2)
        next_page = driver.find_element_by_css_selector('.page.next.S_txt1.S_line1')
        next_href = next_page.get_attribute('href')

        # userfile.write(u'用户:'+user_id+u'关注的用户如下：')
        # userfile.write("\n")

        page_num = 0
        # 如果存在下一页
        while next_href != None and page_num < 5:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.W_f14.S_txt1')))
            # 获取当前页面的所有关注人
            username_list = driver.find_elements_by_class_name('mod_info')
            if len(username_list) == 0:
                username_list = driver.find_element_by_css_selector('.follow_item.S_line2')
            for username in username_list:
                username = username.find_element_by_class_name('S_txt1')
                url = username.get_attribute('href')
                # 获得用户id
                force_user_id = url.split('?')[0].split('/')[-1]
                userfile.write(force_user_id)
                userfile.write("\n")

            user_list.append(list)
            # 获取下一页
            next_page = driver.find_element_by_css_selector('.page.next.S_txt1.S_line1')
            next_href = next_page.get_attribute('href')
            # 如果下一页存在连接
            if next_href != None:
                driver.get(next_href)
            time.sleep(2)
            page_num += 1
    except Exception as e:
        print(e.args)

        # len(user_list)


if __name__ == '__main__':
    # 定义变量
    username = "aaa"
    password = 'bbb'
    user_id = "ccc"

    # 登陆微博
    LoginWeibo(username, password)

    # 得到当前用户所有关注用户的id
    #
    # userfile=codecs.open('User-%s.txt'%user_id,'r','utf-8')
    # for line in userfile.readlines():
    #     print line.strip('\n')
    #     get_force_user(line.strip('\n'))
    #     #获取这些用户发送的微博
    #     VisitPersonPage(line.strip('\n'))

    VisitPersonPage('shihuiapp')


    # 1.根据当前用户，获取所有关注的用户
    # 2.所有用户发布的微博
