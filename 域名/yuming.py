# -*- coding:utf-8 -*-
# 自动获取未注册的域名
import codecs
import json
import multiprocessing
import random
from multiprocessing.pool import Pool

import requests
import time

a = 'a ai an ang ao'
b = 'ba bo bao bai bei bao ban ben bang beng bi bie biao bian bin bing'
c = 'ca cai can cang cao ce cen ceng cha chai chan chang chao che chen cheng chi chong chou chu chua chuai chuan chui chun chuo ci cong cou cu cuan cui cun cuo'
d = 'da dai dan dang dao de dei den deng di dia dian diao die ding diu dong dou du duan dui dun duo'
e = 'e ei en eng er'
f = 'fa fo fei fou fu fan fen fang feng'
g = 'ga gai gan gang gao ge gei gen geng gong gou gu gua guai guan guang gui gun guo'
h = 'ha hai han hang hao he hei hen heng hong hou hu hua huai huan huang hui hun huo'
j = 'ji jia jian jiang jiao jie jin jing jiong jiu ju juan jue jun'
k = 'ka kai kan kang kao ke ken keng kong kou ku kua kuai kuan kuang kui kun kuo'
l = 'la lai lan lang lao le lei leng li lia lian liang liao lie lin ling liu lo long lou lu luan lun luo lv lve'
m = 'ma mai man mang mao me mei men meng mi mian miao mie min ming miu mo mou mu'
n = 'na nai nan nang nao ne nei nen neng ni nian niang niao nie nin ning niu nong nou nu nuan nun nuo nv nve'
o = 'o ou'
p = 'pa pai pan pang pao pei pen peng pi pian piao pie pin ping po pou pu'
q = 'qi qia qian qiang qiao qie qin qing qiong qiu qu quan que qun'
r = 'ran rang rao re ren reng ri rong rou ru ruan rui run ruo'
s = 'sa sai san sang sao se sen seng sha shai shan shang shao she shen sheng shi shou shu shua shuai shuan shuang shui shun shuo si song sou su suan sui sun suo'
t = 'ta tai tan tang tao te teng ti tian tiao tie ting tong tou tu tuan tui tun tuo'
w = 'wa wai wan wang wei wen weng wo wu'
x = 'xi xia xian xiang xiao xie xin xing xiong xiu xu xuan xue xun'
z = 'za zai zan zang zao ze zei zen zeng zha zhai zhan zhang zhao zhe zhei zhen zheng zhi zhong zhou zhu zhua zhuai zhuan zhuang zhui zhun zhuo zi zong zou zu zuan zui zun zuo'
y = 'ya yan yang yao ye yi yin ying yo yong you yu yuan yue yun'

list = [b, c, d, e, f, g, h, j, k, l, m, n, o, p, q, r, s, t, x, y, z, w]


# 随机生成汉字组合
def getRndStrSByHanzi(num):
    code_list = []
    for hanyu in list:
        h_list = hanyu.split(' ')
        code_list.extend(h_list)

    myslice = random.sample(code_list, num)  # 从list中随机获取6个元素，作为一个片断返回
    verification_code = ''.join(myslice)  # list to string
    return verification_code


# 随机生成纯字母
def getRndStrSByZimu(num):
    code_list = []
    # for i in range(10): # 0-9数字
    #     code_list.append(str(i))
    for i in range(65, 91):  # A-Z
        code_list.append(chr(i))
    for i in range(65, 91):  # A-Z
        code_list.append(chr(i))
    for i in range(97, 122):  # a-z
        code_list.append(chr(i))
    myslice = random.sample(code_list, num)  # 从list中随机获取6个元素，作为一个片断返回
    verification_code = ''.join(myslice)  # list to string
    return verification_code

# 字母和数字的组合
def getRndStrSByZimuAndShuzi(num):
    code_list = []
    for i in range(10):  # 0-9数字
        code_list.append(str(i))
    for i in range(65, 91):  # A-Z
        code_list.append(chr(i))
    for i in range(65, 91):  # A-Z
        code_list.append(chr(i))
    for i in range(97, 122):  # a-z
        code_list.append(chr(i))
    myslice = random.sample(code_list, num)  # 从list中随机获取6个元素，作为一个片断返回
    verification_code = ''.join(myslice)  # list to string
    return verification_code


def getRndStrSByShuzi(num):
    code_list = []
    for i in range(10):  # 0-9数字
        code_list.append(str(i))
    for i in range(10):  # 0-9数字
        code_list.append(str(i))
    for i in range(10):  # 0-9数字
        code_list.append(str(i))
    for i in range(10):  # 0-9数字
        code_list.append(str(i))
    myslice = random.sample(code_list, num)  # 从list中随机获取6个元素，作为一个片断返回
    verification_code = ''.join(myslice)  # list to string
    return verification_code



comlist = {'.com', '.cn'}


# 每次检查10000条数据


def queryHanzi(num):
    for j in range(10000):
        name = getRndStrSByHanzi(num)
        query_yuming(name)
        time.sleep(0.5)


def queryZimu(num):
    for j in range(10000):
        name = getRndStrSByZimu(num)
        query_yuming(name)
        time.sleep(0.5)


def queryZiAndNum(num):
    for j in range(10000):
        name = getRndStrSByZimuAndShuzi(num)
        query_yuming(name)
        time.sleep(0.5)


def queryShuzi(num):
    for j in range(10000):
        name = getRndStrSByShuzi(num)
        query_yuming(name)
        time.sleep(0.5)


def query_yuming(name):
    for k in comlist:
        url = 'https://checkapi.aliyun.com/check/checkdomain?callback=jQuery1111021145157480983423_1502690951996&domain={0}{1}&token=check-web-hichina-com%3A8yjfr0yfncavu2t8ps0fn0x4f4kwbcnf&_=1502690952063'.format(
            name, k)
        # url='https://checkapi.aliyun.com/check/checkdomain?callback=jQuery1111031362323538242776_1502440498572&domain={0}{1}&token=check-web-hichina-com%3Afqd679szpeyp5m1zjfajcpuzipcuadfl&_=1502440498639'.format(name,k)
        r = requests.get(url)

        # print(r.text)
        r=r.text.replace('(','-')
        r=r.replace(')','-')
        result=json.loads(str(r.split('-')[1]))
        if result['module'][0]['avail']==1:
            print(name.lower() + k)
            # infofile = open('yuming.txt', 'a+')
            with open('yuming.txt', 'a+') as infofile:
                infofile.write(name.lower() + k + '\n')

    # infofile.close()

if __name__ == '__main__':
    ps=Pool(1)
    # 从字母列表中随机取两个
    # ps.apply_async(queryHanzi,(2,))
    ps.apply_async(queryZimu,(4,))
    # p1=multiprocessing.Process(target=queryHanzi,args=(3,))
    # p2 = multiprocessing.Process(target=queryHanzi, args=(2,))
    # p3=multiprocessing.Process(target=queryZiAndNum,args=(4,))
    # p4=multiprocessing.Process(target=queryShuzi,args=(4,))

    # p2.start()
    # p2.start()
    # p3.start()
    # p4.start()
    ps.close()
    ps.join()
