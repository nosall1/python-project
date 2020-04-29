#-*- coding:utf-8 -*-
import random

from bs4 import BeautifulSoup
import requests
start_url='https://bj.58.com/sale.shtml?utm_source=market&spm=u-2d2yxv86y3v43nkddh1.BDPCPZ_BT&PGTID=0d100000-0000-1a87-6276-6825efeb0952&ClickID=4'
url_host='https://bj.58.com'
headers={
    "User-Agent":'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36',
    "Connection":"keep-alive"
}
proxy_list=[
    {'http':'180.118.128.73:9000'},
    {'http':'60.168.206.111:1133'},
    {'http':'117.69.153.98:9999'},
]

channel_list=[]
def get_channel_urls(url):
    print(random.choice(proxy_list))
    wb_data=requests.get(url,headers,proxies=random.choice(proxy_list))
    soup=BeautifulSoup(wb_data.text,'lxml')
    links=soup.select("ul.ym-submnu > li>span>a")
    for link in links:
        page_url=url_host+link.get('href')
        channel_list.append(page_url)
    print(channel_list)
get_channel_urls(start_url)