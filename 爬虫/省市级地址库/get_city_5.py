#-*- coding:utf-8 -*-
# 爬取国家统计局省、市、区、街道、办事处五级地址

import datetime
import json
import os
import threading

import requests
from bs4 import BeautifulSoup


class GetCity(object):

    url='http://www.stats.gov.cn/tjsj/tjbz/tjyqhdmhcxhfdm/2017/'

    def __init__(self):
        self.json_folder='json'
        self.json_file={'province':'province.json','city':'city.json','county':'county.json','town':"town.json",'village':'village.json'}
        self.lock=threading.Lock()

    def get_html(self,url):
        headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36'
        }
        try:
            result=requests.get(url=url,headers=headers)
            result.encoding='gbk'
            html=result.text
            return html
        except Exception as e:
            return ''

        # 解析省份信息
    def get_province(self,origin_url):
        print('开始解析省份信息...')
        html=self.get_html(origin_url)
        soup=BeautifulSoup(html,'html.parser')
        province_list=soup.select('.provincetr a')
        for province_info in province_list:
            province_name=province_info.get_text()
            province_url=province_info.attrs['href']
            province_code=province_url.split('.')[0]
            print(province_name,province_code,province_url)

            dict_info={}
            dict_info.update({'name':province_name})
            dict_info.update({'code':province_code})
            dict_info.update({'parent_code':'0'})
            dict_info.update({'level':"1"})
            self.read_write_by_json(dict_info,'province')

            # self.get_city(origin_url,province_url,province_code)
            # 多线程爬取,每个省份一个线程
            t=threading.Thread(target=self.get_city,name='LoopThread',args=(origin_url,province_url,province_code))
            t.start()
        print('省份解析结束')

    # 请求市级地址信息
    def get_city(self,origin_url,now_url,origin_code):
        province_url=origin_url+now_url
        print('开始解析市级信息')
        html=self.get_html(province_url)
        soup=BeautifulSoup(html,'html.parser')
        city_list=soup.select('.citytr')
        for city_info in city_list:
            a_info=city_info.find_all('a')
            city_name=a_info[1].get_text()
            city_code=a_info[0].get_text()
            city_url=a_info[0].attrs['href']
            print(city_name,city_code,city_url)
            dict_info={}
            dict_info.update({'name':city_name})
            dict_info.update({'code':city_code})
            dict_info.update({'parent_code':origin_code})
            dict_info.update({'level':2})

            self.read_write_by_json(dict_info,'city')
            # 获取显区信息
            self.get_county(origin_url,city_url,city_code)
        print('市级解析结束')

    # 获取县，区级地址信息
    def get_county(self,origin_url,now_url,origin_code):
        city_url=origin_url+now_url
        print('开始解析县/区级信息...')
        html=self.get_html(city_url)
        soup=BeautifulSoup(html,'html.parser')
        county_list=soup.select('.countytr')
        for county_info in county_list:
            a_info=county_info.find_all('a')
            if a_info:
                county_name=a_info[1].get_text()
                county_code=a_info[0].get_text()
                county_url=a_info[0].attrs['href']
                print(county_name,county_code,county_url)
                dict_info={}
                dict_info.update({'name':county_name})
                dict_info.update({'code':county_code})
                dict_info.update({'parent_code':origin_code})
                dict_info.update({'level':3})
                self.read_write_by_json(dict_info,'county')
                # 拼接下一级的前缀
                # url=origin_url+now_url.split('/')[0]+'/'
                city_url='/'.join(city_url.split('/')[:-1])+'/'
                self.get_town(city_url,county_url,county_code)
            else:
                td_info=county_info.find_all('td')
                county_name=td_info[1].get_text()
                county_code=td_info[0].get_text()
                county_url=''
                print(county_name,county_code,county_url)
        print('县/区级解析结束')

    # 获取乡镇地址信息
    def get_town(self,origin_url,now_url,origin_code):
        county_url=origin_url+now_url
        print('开始解析乡镇级信息...')
        html=self.get_html(county_url)
        soup=BeautifulSoup(html,'html.parser')
        town_list=soup.select('.towntr')
        for town_info in town_list:
            a_info=town_info.find_all('a')
            town_name=a_info[1].get_text()
            town_code=a_info[0].get_text()
            town_url=a_info[0].attrs['href']
            print(town_name,town_code,town_url)
            dict_info={}
            dict_info.update({'name':town_name})
            dict_info.update({'code':town_code})
            dict_info.update({'parent_code':origin_code})
            dict_info.update({'level':4})
            self.read_write_by_json(dict_info,'town')
            # 拼接下一级的前缀
            county_url='/'.join(county_url.split('/')[:-1])+'/'
            # 获取村级信息
            self.get_village(county_url,town_url,town_code)
        print('乡镇级解析结束')

    # 获取村级地址信息
    def get_village(self,origin_url,now_url,origin_code):
        town_url=origin_url+now_url
        print('开始解析村级信息...')
        html=self.get_html(town_url)
        soup=BeautifulSoup(html,'html.parser')
        village_list=soup.select('.villagetr')
        for village_info in village_list:
            a_info=village_info.find_all('td')
            village_name=a_info[2].get_text()
            village_code=a_info[0].get_text()
            village_url=''
            print(village_name,village_code,village_url)
            dict_info={}
            dict_info.update({'name':village_name})
            dict_info.update({'code':village_code})
            dict_info.update({'parent_code':origin_code})
            dict_info.update({'level':5})
            self.read_write_by_json(dict_info,'village')
        print('村级解析结束')

    def init_file(self):
        if not os.path.exists(self.json_folder):
            os.mkdir(self.json_folder)

        for file_name in self.json_file.values():
            file_path=os.path.join(self.json_folder,file_name)
            if not os.path.exists(file_path):
                with open(file_path,'w',encoding='utf-8') as file:
                    json.dump([],file)

    # 读写json文件
    def read_write_by_json(self,data,city_type):
        self.lock.acquire()
        file_name=self.json_file[city_type]
        file_path=os.path.join(self.json_folder,file_name)
        # 读取文件
        if os.path.getsize(file_path)==0:
            data_list={}
        else:
            with open(file_path,'r',encoding='utf-8') as read_file:
                data_list=json.load(read_file)
                data_list.append(data)
            # 写文件
        with open(file_path,'w',encoding='utf-8') as write_file:
            json.dump(data_list,write_file,ensure_ascii=False)
        self.lock.release()



    def run(self):
        self.init_file()
        self.get_province(self.url)

if __name__ == '__main__':
    # 实例化执行
    print('开始执行……')
    start_time = datetime.datetime.now()
    city = GetCity()
    city.run()
    end_time = datetime.datetime.now()
    print('程序执行结束！')
    print('开始时间：%s，结束时间：%s' % (start_time.strftime('%Y-%m-%d %H:%M:%S'), end_time.strftime('%Y-%m-%d %H:%M:%S')))