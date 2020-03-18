#-*- coding:utf-8 -*-
import requests
import os
from bs4 import BeautifulSoup

class Skin(object):
    def __init__(self):
        # 英雄的json数据
        self.hero_url='http://pvp.qq.com/web201605/js/herolist.json'
        # 英雄详细页的通用url前缀信息
        self.base_url='https://pvp.qq.com/web201605/herodetail/'
        # 英雄详细页url后缀信息
        self.detail_url=''
        # 图片存储文件夹
        self.img_folder='skin'
        # 图片url的通用前缀
        self.skin_url='https://game.gtimg.cn/images/yxzj/img201606/skin/hero-info/'
        # 图片url的后缀信息
        self.skin_detail_url=''

    def get_hero(self):
        # 获取英雄的json数据
        req=requests.get(self.hero_url)
        # 将返回值转换为json数据
        hero_list=req.json()
        return hero_list
    def get_hero_skin(self,hero_name,hero_no):
        # 获取详细页英雄皮肤展示的信息，并爬图
        url=self.base_url+self.detail_url
        req=requests.get(url)
        req.encoding='gbk'
        html=req.text
        # 获取皮肤信息的节点
        soup=BeautifulSoup(html,'html.parser')
        skip_list=soup.select(".pic-pf-list3")
        for skin_info in skip_list:
            # 获取皮肤名称
            img_names=skin_info.attrs['data-imgname']
            name_list=img_names.split('|')
            skin_no=1
            # 循环下载皮肤图片
            for skin_name in name_list:
                self.skin_detail_url="%s/%s-bigskin-%s.jpg" %(hero_no,hero_no,skin_no)
                skin_no+=1
                img_name=hero_name+"-"+skin_name+".jpg"
                self.download_skin(img_name)
    # 下载皮肤图片
    def download_skin(self,img_name):
        img_url=self.skin_url+self.skin_detail_url
        req=requests.get(img_url)
        if req.status_code==200:
            print('download-%s'%img_name)
            img_path=os.path.join(self.img_folder,img_name)
            with open(img_path,'wb') as img:
                img.write(req.content)
        else:
            print("img error")
    # 创建图片存储文件夹
    def make_folder(self):
        if not os.path.exists(self.img_folder):
            os.mkdir(self.img_folder)

    def run(self):
        self.make_folder()
        hero_list=self.get_hero()
        for hero in hero_list:
            hero_no=str(hero['ename'])
            self.detail_url=hero_no+".shtml"
            hero_name=hero['cname']
            self.get_hero_skin(hero_name,hero_no)

if __name__ == '__main__':
    skin = Skin()
    skin.run()