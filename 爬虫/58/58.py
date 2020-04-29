#-*- coding:utf-8 -*-
from multiprocessing.pool import Pool

import pymongo
import random
import time

from bs4 import BeautifulSoup
import requests
class spider_58:
    headers={
        "User-Agent":'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36',
        "Connection":"keep-alive"
    }


    def __init__(self):
        self.channel_list=[]
        self.url_host='https://bj.58.com'
        self.proxies=''
        self.conn_mongo()

    # 获取代理ip
    def get_proxy_ip(self):
        proxy_list=[
            'http://175.42.129.217:9999',
            'http://223.242.225.223:9999',
            'http://123.169.34.163:9999',
            'http://175.24.18.94:8888',
        ]
        proxy_ip=random.choice(proxy_list)
        self.proxies={'http':proxy_ip}

    def conn_mongo(self):
        client=pymongo.MongoClient('localhost',27017)
        # 创建表
        ceshi=client['ceshi']
        # 创建库
        self.url_list=ceshi['url_list']
        self.item_info=ceshi['item_info']

    # 获取频道的url
    def get_channel_urls(self,url):
        wb_data=requests.get(url,self.headers)
        soup=BeautifulSoup(wb_data.text,'lxml')
        links=soup.select("ul.ym-submnu > li>span>a")
        for link in links:
            page_url=self.url_host+link.get('href')
            self.channel_list.append(page_url)
        print(self.channel_list)

    # 一个频道下商品的所有连接
    def get_links_from(self,channel,pages,who_sells=0):
        self.get_proxy_ip()
        # list_view='https://bj.58.com/iphonesj/0/pn1'
        list_view='{}{}/pn{}/'.format(channel,str(who_sells),str(pages))
        wb_data=requests.get(list_view,headers=self.headers,proxies=self.proxies)
        time.sleep(1)
        soup=BeautifulSoup(wb_data.text,'lxml')
        if soup.find('td','t'):
            for link in soup.select('td.t a.t'):
                item_link=link.get('href').split('?')[0]
                self.url_list.insert_one({"url":item_link})
        else:
            pass

    # 获取商品详情
    def get_item_info(self,url):
        self.get_proxy_ip()
        wb_data=requests.get(url,headers=self.headers,proxies=self.proxies)
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
            self.item_info.insert_one({"title":title,"price":price,"date":date,"area":area})

    def get_all_links_from(self,channel):
        for num in range(1,101):
            print(1)
            self.get_links_from(channel,num)


    def run(self):

        pool=Pool()
        pool.map(self.get_all_links_from,self.channel_list)

if __name__ == '__main__':
    spider_58=spider_58()
    start_url='https://bj.58.com/sale.shtml?utm_source=market&spm=u-2d2yxv86y3v43nkddh1.BDPCPZ_BT&PGTID=0d100000-0000-1a87-6276-6825efeb0952&ClickID=4'
    spider_58.get_channel_urls(start_url)
    # spider_58.run()