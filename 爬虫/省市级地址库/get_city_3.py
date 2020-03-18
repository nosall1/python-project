#-*- coding:utf-8 -*-

# 省市级三级地址库
import json,os

import requests
from bs4 import BeautifulSoup


def get_provine(index_href):
    print('开始抓取省份信息...')
    province_url=url+index_href
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
    }
    result=requests.get(province_url,headers=headers)
    result.encoding='gbk'
    province_html_text=str(result.text)
    soup=BeautifulSoup(province_html_text,'html.parser')
    province_tr_list=soup.select('.provincetr a')
    province_list={}
    province_key=0
    # 遍历省份列表信息
    for province_tr in province_tr_list:
        if province_tr:
            province_href=province_tr.attrs['href']
            province_no=province_href.split('.')[0]
            province_code=province_no+'0000'
            province_name=province_tr.text
            province_info={'code':province_code,'name':province_name}
            province_list.setdefault(province_key,province_info)
            province_key+=1
            print("已写入省级：",province_code)
            # 市级
            get_city(province_href,province_code)

    print('抓取省份信息结束')
    file=open('json/province.json','w',encoding='utf-8')
    json.dump(province_list,file,ensure_ascii=False)
    file.close()


# 抓取市级城市信息
def get_city(province_href,province_code):
    print('开始抓取市级信息')
    city_url=url+province_href
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
    }
    result=requests.get(city_url,headers=headers)
    result.encoding='gbk'
    city_html_text=str(result.text)
    soup=BeautifulSoup(city_html_text,'html.parser')
    city_tr_list=soup.select('.citytr')
    if os.path.exists('json/city.json'):
        file=open('json/city.json','r',encoding='utf-8')
        city_data=json.load(file)
        file.close()
    else:
        city_data={}
    city_list={}
    city_key=0
    # 遍历市级城市列表信息
    for city_tr in city_tr_list:
        if city_tr:
            city_a_info=city_tr.select('a')
            city_href=city_a_info[0].attrs['href']
            city_code=city_a_info[0].text[:6]
            city_name=city_a_info[1].text
            city_info={'code':city_code,'name':city_name}
            city_list.setdefault(city_key,city_info)
            city_key+=1
            print('已写入市级：',city_info)
            # 区级
            get_area(city_href,city_code)

    city_data.setdefault(province_code,city_list)
    print('抓取市级城市结束')
    file=open('json/city.json','w',encoding='utf-8')
    json.dump(city_data,file,ensure_ascii=False)
    file.close()

# 抓取区级信息
def get_area(city_href,city_code):
    print('开始抓取区级信息')
    area_url=url+city_href
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
    }
    result=requests.get(area_url,headers=headers)
    result.encoding='gbk'
    area_html_text=str(result.text)
    soup=BeautifulSoup(area_html_text,'html.parser')
    area_tr_list=soup.select('.countytr')
    if os.path.exists("json/area.json"):
        file=open('json/area.json','r',encoding='utf-8')
        area_data=json.load(file)
        file.close()
    else:
        area_data={}

    area_list={}
    area_key=0
    # 遍历区级列表信息
    for area_tr in area_tr_list:
        area_a_info=area_tr.select('td')
        if area_a_info:
            area_code=area_a_info[0].text[:6]
            area_name=area_a_info[1].text
            area_info={'code':area_code,'name':area_name}
            area_list.setdefault(area_key,area_info)
            area_key+=1
            print('已写入区级：',area_info)

    area_data.setdefault(city_code,area_list)
    print('抓取区级信息结束')
    file=open('json/area.json','w',encoding='utf-8')
    json.dump(area_data,file,ensure_ascii=False)
    file.close()

if __name__ == '__main__':
    url='http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2017/'
    json_folder='json'
    if not os.path.exists(json_folder):
        os.makedirs(json_folder)
    get_provine('index.html')