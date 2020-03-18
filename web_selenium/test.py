# -*- coding:utf-8 -*-
import io
import time
import uuid


from selenium import webdriver
from PIL import Image, ImageChops
from selenium.webdriver import ActionChains, DesiredCapabilities


class BaseGeetestCrack(object):

    """验证码破解基础类"""

    def __init__(self, driver):
        self.driver = driver
        # self.driver.maximize_window()

    def input_by_id(self, text=u"中国移动", element_id="keyword_qycx"):
        """输入查询关键词
        :text: Unicode, 要输入的文本
        :element_id: 输入框网页元素id
        """
        input_el = self.driver.find_element_by_id(element_id)
        input_el.clear()
        input_el.send_keys(text)
        time.sleep(3.5)

    def click_by_id(self, element_id="popup-submit"):
        """点击查询按钮
        :element_id: 查询按钮网页元素id
        """
        search_el = self.driver.find_element_by_id(element_id)
        search_el.click()
        time.sleep(3.5)

    def calculate_slider_offset(self):
        """计算滑块偏移位置，必须在点击查询按钮之后调用
        :returns: Number
        """
        img1=Image.open('1.png')
        img2 = self.crop_captcha_image()
        # img2=Image.open('3.png')

        width, height = img1.size

        self.get_offset_distance(img2,img1)
        # w2, h2 = img2.size
        # if w1 != w2 or h1 != h2:
        #     return False

        # for h in range(1, h1):
        #     for w in range(0, w1):
        #         pixel2 = img1.getpixel((w, h))
        #         pixel1 = img2.getpixel((w, h))
        #         if ((pixel2[0]+pixel2[1]+pixel2[2])-(pixel1[0]+pixel1[1]+pixel1[2]))>300:
        #             print(w)
        #             return w

        for h in range(1, height):
            # print('')
            for w in range(0, width-20):
                flag1=True

                if ((img1.getpixel((w, h))[0]+img1.getpixel((w, h))[1]+img1.getpixel((w, h))[2])-(img2.getpixel((w, h))[0]+img2.getpixel((w, h))[1]+img2.getpixel((w, h))[2]))<-50:
                    for i in range(20):
                        if ((img1.getpixel((w+i, h))[0]+img1.getpixel((w+i, h))[1]+img1.getpixel((w+i, h))[2])-(img2.getpixel((w+i, h))[0]+img2.getpixel((w+i, h))[1]+img2.getpixel((w+i, h))[2]))>-50:
                            flag1=False

                    if flag1==True:
                        w=w+20
                        for w1 in range(w, width-20):
                            flag2=True
                            if ((img1.getpixel((w1, h))[0]+img1.getpixel((w1, h))[1]+img1.getpixel((w1, h))[2])-(img2.getpixel((w1, h))[0]+img2.getpixel((w1, h))[1]+img2.getpixel((w1, h))[2]))>30:
                                for j in range(20):
                                    if ((img1.getpixel((w1+j, h))[0]+img1.getpixel((w1+j, h))[1]+img1.getpixel((w1+j, h))[2])-(img2.getpixel((w1+j, h))[0]+img2.getpixel((w1+j, h))[1]+img2.getpixel((w1+j, h))[2]))<30:
                                        flag2=False
                                        break

                                if flag1 and flag2:
                                    print('-----',str(w1),str(h))
                                    return w1

    def is_pixel_equal(self, img1, img2, x, y):
        pix1 = img1.load()[x, y]
        pix2 = img2.load()[x, y]
        if (abs(pix1[0] - pix2[0] < 60) and abs(pix1[1] - pix2[1] < 60) and abs(pix1[2] - pix2[2] < 60)):
            return True
        else:
            return False

    def crop_captcha_image(self):
        """截取验证码图片
        :element_id: 验证码图片网页元素id
        :returns: StringIO, 图片内容
        """

        # self.driver.get_screenshot_as_file('loggin.png')
        self.driver.get_screenshot_as_file('loggin.png')
        # captcha_el = self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[6]/div/div[1]/div[1]/div/a/div[1]/div/canvas[2]')
        captcha_el = self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[6]/div/div[1]/div[1]/div/a/div[1]')

        location = captcha_el.location
        size = captcha_el.size
        left = int(location['x'])*2
        top = int(location['y'])*2
        # left = 1350
        # top = 564
        right = left + int(size['width'])*2
        bottom = top + int(size['height'])*2
        # right = left + 516
        # bottom = top + 320
        print(left, top, right, bottom)

        time.sleep(1)
        screenshot = Image.open('loggin.png')
        captcha = screenshot.crop((left, top, right, bottom))
        captcha.save("11.png")
        return captcha

    def get_browser_name(self):
        """获取当前使用浏览器名称
        :returns: TODO
        """
        return str(self.driver).split('.')[2]

    def drag_and_drop(self, x_offset=0, y_offset=0):
        """拖拽滑块
        :x_offset: 相对滑块x坐标偏移
        :y_offset: 相对滑块y坐标偏移
        :element_class: 滑块网页元素CSS类名
        """
        dragger = self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/div[6]/div/div[1]/div[2]/div[2]')
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(dragger, x_offset, y_offset).perform()
        # 这个延时必须有，在滑动后等待回复原状
        time.sleep(8)

    def move_to_element(self, element_class="gt_slider_knob"):
        """鼠标移动到网页元素上
        :element: 目标网页元素
        """
        time.sleep(3)
        element = self.driver.find_element_by_class_name(element_class)
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()
        time.sleep(4.5)


    def login(self, username, password):
        # 登录
        login_element = self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[1]/div/div[5]/div[2]/a[1]/button')
        login_element.click()
        time.sleep(3)
        # 用户名
        name_element = self.driver.find_element_by_name('email')
        # 密码
        password_element = self.driver.find_element_by_name('password')

        name_element.send_keys(username)
        password_element.send_keys(password)

        # 提交按钮
        submit_element = self.driver.find_element_by_xpath('//*[@id="root"]/div/div/div/div[2]/div/div/form[1]/div/div[3]/div/button')
        submit_element.click()
        time.sleep(10)


    # 判断颜色是否相近
    def is_similar_color(self, x_pixel, y_pixel):
        for i, pixel in enumerate(x_pixel):
            if abs(y_pixel[i] - pixel) > 50:
                return False
        return True

    # 计算距离
    def get_offset_distance(self, cut_image, full_image):
        for x in range(cut_image.width):
            for y in range(cut_image.height):
                cpx = cut_image.getpixel((x, y+10))
                fpx = full_image.getpixel((x, y+10))
                if not self.is_similar_color(cpx, fpx):
                    img = cut_image.crop((x, y, x + 50*2, y + 40*2))
                    # 保存一下计算出来位置图片，看看是不是缺口部分
                    img.save("2.png")
                    return x


# option = webdriver.ChromeOptions()
# option.add_argument('headless')
# driver = webdriver.Chrome(chrome_options=option)

driver=webdriver.Chrome()
url = '***'
driver.get(url)
# driver.set_window_size(1608, 950)
driver.maximize_window()
otp_button=driver.find_element_by_xpath('/html/body/div[5]/div/div/div/span')
otp_button.click()
time.sleep(5)

user_name='***'
password='***'

base=BaseGeetestCrack(driver)
base.login(user_name,password)
x_offset=base.calculate_slider_offset()
base.drag_and_drop(x_offset/2)




# img1=Image.open('1.png')
# img2=Image.open('3.png')
# width = img1.size[0]
# height = img1.size[1]
# tip=[]
# count = 0
#
# for h in range(1, height):
#     print('')
#     for w in range(0, width-20):
#         flag=True
#         if ((img1.getpixel((w, h))[0]+img1.getpixel((w, h))[1]+img1.getpixel((w, h))[2])-(img2.getpixel((w, h))[0]+img2.getpixel((w, h))[1]+img2.getpixel((w, h))[2]))>20:
#             for i in range(20):
#                 if ((img1.getpixel((w+i, h))[0]+img1.getpixel((w+i, h))[1]+img1.getpixel((w+i, h))[2])-(img2.getpixel((w+i, h))[0]+img2.getpixel((w+i, h))[1]+img2.getpixel((w+i, h))[2]))<20:
#                     flag=False
#             if flag==True:
#                 print('-----',str(w),str(h))




        # print((pixel2[0]+pixel2[1]+pixel2[2])-(pixel1[0]+pixel1[1]+pixel1[2]),end=' ')
        # if count==0:
        #     if (pixel2[0]+pixel2[1]+pixel2[2])-(pixel1[0]+pixel1[1]+pixel1[2])>20:
        #         pixel2 = img1.getpixel((w+1, h))
        #         pixel1 = img2.getpixel((w+1, h))


