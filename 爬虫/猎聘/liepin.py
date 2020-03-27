#-*- coding:utf-8 -*-
# 抓取猎聘的职位
import time
import threading

import requests
import re
from bs4 import BeautifulSoup
def get_job_list(job):
    thread_name = threading.current_thread().name
    print(f'[{thread_name}]:{job}')
    page_num=0
    while True:
        url='https://www.liepin.com/city-bj/zhaopin/pn'+str(page_num)+'/?key='+job+'&d_sfrom=search_city&d_ckId=757adc2153c6034f3c9d7fc1970e617d&d_curPage=1&d_pageSize=40&d_headId=757adc2153c6034f3c9d7fc1970e617d'
        resp=requests.get(url)
        soup=BeautifulSoup(resp.text,'html.parser')
        try:
            for div in soup.find_all('div',class_='sojob-item-main clearfix'):
                print(div.find('a').text,end=' ')
                xinzi= div.find('span',class_='text-warning')
                print(xinzi.next,end=' ')
                area=div.find('a',class_='area')
                edu= div.find('span',class_='edu')
                print(area.text,end=' ')
                print(edu.next)
        except Exception as e:
            print(e)

        div=soup.find('a',string=re.compile('下一页'))
        if div:
            print(div.text)
            print(page_num)
        else:
            break
        time.sleep(1)
        page_num+=1
# 获取所有的职位类型
def get_all_job_type():
    url='https://www.liepin.com/city-bj/zhaogongzuo/?sfrom=click-pc_homepage-centre_keywordjobs-search_new'
    resp=requests.get(url)
    soup=BeautifulSoup(resp.text,'html.parser')
    all_list=[]
    for dd in soup.find_all('dd'):
        a_all=dd.find_all('a')
        for a in a_all:
            # print(a.text)
            all_list.append(a.text)
    job_list=all_list[:-21]
    return job_list


job_list=get_all_job_type()
for job in job_list:
    print(job)
    t=threading.Thread(target=get_job_list,args=(job,))
    t.start()
