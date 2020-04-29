#-*- coding:utf-8 -*-
import random

from bs4 import BeautifulSoup
import requests
import time
import pymongo

client=pymongo.MongoClient('localhost',27017)
# 创建表
ceshi=client['ceshi']
# 创建库
url_list=ceshi['url_list']
item_info=ceshi['item_info']


headers={
    "User-Agent":'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36',
    "Connection":"keep-alive"
}
proxy_list=[
    'http://175.42.129.217:9999',
    'http://223.242.225.223:9999',
    'http://123.169.34.163:9999',
    'http://175.24.18.94:8888',
]

proxy_ip=random.choice(proxy_list)

proxies={'http':proxy_ip}
# 查询商品连接
def get_links_from(channel,pages,who_sells=0):
    # list_view='https://bj.58.com/iphonesj/0/pn1'
    list_view='{}{}/pn{}/'.format(channel,str(who_sells),str(pages))
    wb_data=requests.get(list_view,headers=headers,proxies=proxies)
    time.sleep(1)
    soup=BeautifulSoup(wb_data.text,'lxml')
    if soup.find('td','t'):
        for link in soup.select('td.t a.t'):
            item_link=link.get('href').split('?')[0]
            url_list.insert_one({"url":item_link})
    else:
        pass


def get_item_info(url):
    wb_data=requests.get(url,headers=headers,proxies=proxies)
    soup=BeautifulSoup(wb_data.text,'lxml')
    no_longer_exist='404' in soup.find('script',type='text/javascript').get('src').split('/')
    # 如果页面不存在了
    if no_longer_exist:
        pass
    else:
        title=soup.title.text
        price=soup.select('span.infocard__container__item__main__text--price')[0].text.replace("\t",'').replace("\n",'').replace("\r",'')
        date=soup.select('div.detail-title__info__text')[0].text.split(" ")[0]
        area=soup.select('div.infocard__container__item__main > a')[0].text
        item_info.insert_one({"title":title,"price":price,"date":date,"area":area})
