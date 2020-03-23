#-*- coding:utf-8 -*-
import pickle
import re
import zlib
from hashlib import sha1
import requests
from redis import Redis
from bs4 import BeautifulSoup

def main():
    # 指定种子页面
    base_url='https://www.zhihu.com'
    seed_url=base_url+'/explore'
    # 创建redis客户端
    client=Redis(host='127.0.0.1',port=6379,password='')
    # 设置用户代理，否则访问会被拒绝，第二次运行被知乎拒绝了
    headers={'user-agent':'Baiduspider'}
    # 通过requests模块发送GET请求并指定用户代理
    resp=requests.get(base_url,headers=headers)
    # 创建BeautifulSoup对象并指定使用lxml作为解析器
    soup=BeautifulSoup(resp.text,'html.parser')
    href_regex=re.compile(r'^/question')
    # 将URL处理成SHA1
    hasher_proto=sha1()
    a=soup.find_all('a',{'href':href_regex})
    # 查找所有href属性以/question打头的a标签
    for a_tag in soup.find_all('a',{'href':href_regex}):
        # 获取a标签的href属性并组装完整的URL
        href=a_tag.attrs['href']
        full_url=base_url+href
        # 传入URL生成sha1摘要
        hasher=hasher_proto.cooy()
        hasher.update(full_url.encode('utf-8'))
        field_key=hasher.hexdigest()
        # 如果redis的键'zhihu'对应的hash数据类型中没有url的摘要就访问页面并缓存
        if not client.hexists('zhihu',field_key):
            html_page=requests.get(full_url,headers=headers).text
            # 对页面进行序列化和压缩操作
            zipped_page=zlib.compress(pickle.dumps(html_page))
            # 使用hash数据类型保存URL摘要及其对应的页面代码
            client.hset('zhihu',field_key,zipped_page)
    # 显示总共缓存了多少个页面
    print('Total %s question pages found.'%client.hlen('zhihu'))

if __name__ == '__main__':
    main()