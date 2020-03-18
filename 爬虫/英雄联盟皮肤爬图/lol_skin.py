#-*- coding:utf-8 -*-

# 抓取LOL英雄皮肤
import json

import requests
import os

class GetLolSkin(object):
    def __init__(self):
        self.hero_url='https://lol.qq.com/biz/hero/champion.js'
        self.hero_detail_url='https://lol.qq.com/biz/hero/'
        self.skin_floder='skin'
        self.skin_url='https://game.gtimg.cn/images/lol/act/img/skinloading/'

    @staticmethod
    def get_html(url):
        # 下载html
        req=requests.get(url)
        req.encoding='gbk'
        if req.status_code==200:
            return req.text
        else:
            return "{}"
    # 获取英雄的完整信息列表
    def get_hero_list(self):

        hero_js=self.get_html(self.hero_url)
        # 删除左右多余的信息，得到json数据
        out_left="if(!LOLherojs)var LOLherojs={};LOLherojs.champion="
        out_right=';'
        hero_list=hero_js.replace(out_left,'').rstrip(out_right)
        return json.loads(hero_list)

    # 获取英雄的详细信息
    def get_hero_info(self,hero_id):
        # 获取js详情
        detail_url=self.hero_detail_url+hero_id+'.js'
        detail_js=self.get_html(detail_url)
        # 删除左右的多余信息，得到json数据
        out_left="if(!herojs)var herojs={champion:{}};herojs['champion'][%s]=" % hero_id
        out_right=';'
        hero_info=detail_js.replace(out_left,'').rstrip(out_right)
        return json.loads(hero_info)
    # 下载皮肤列表
    def download_skin_list(self,skin_list,hero_name):
        for skin_info in skin_list:
            # 拼接图片名字
            if skin_info['name']=='default':
                skin_name='默认皮肤'
            else:
                if ' ' in skin_info['name']:
                    name_info=skin_info['name'].split(' ')
                    skin_name=name_info[0]
                else:
                    skin_name=skin_info['name']

            hero_skin_name=hero_name+"-"+skin_name+".jpg"
            self.download_skin(skin_info['id'],hero_skin_name)
    # 下载皮肤图片
    def download_skin(self,skin_id,skin_name):
        img_url=self.skin_url+skin_id+'.jpg'
        req=requests.get(img_url)
        if req.status_code==200:
            print("downloading...%s"%skin_name)
            img_path=os.path.join(self.skin_floder,skin_name)
            with open(img_path,'wb') as img:
                img.write(req.content)
        else:
            print('img error!')

    # 初始化，创建图片文件夹
    def make_folder(self):
        if not os.path.exists(self.skin_floder):
            os.mkdir(self.skin_floder)

    def run(self):
        hero_json=self.get_hero_list()
        hero_keys=hero_json['keys']
        # 循环遍历英雄
        for hero_id ,hero_code in hero_keys.items():
            hero_name=hero_json['data'][hero_code]['name']
            hero_info=self.get_hero_info(hero_id)
            if hero_info:
                skin_list=hero_info['result'][hero_id]['skins']
                self.download_skin_list(skin_list,hero_name)
            else:
                print("英雄【%s】的皮肤获取有问题"%hero_name)

if __name__ == '__main__':
    lol=GetLolSkin()
    lol.make_folder()
    lol.run()