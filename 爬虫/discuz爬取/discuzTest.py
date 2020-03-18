#-*- coding:utf-8 -*-
import os
import re
import multiprocessing as mp
from lxml import etree


import requests


def StringListSave(save_path,filename,slist):
    if not os.path.exists(save_path):
        os.makedirs(save_path,exist_ok=True)
    path=os.path.join(save_path,filename+'.txt')
    if len(slist)==0:
        print(save_path)
        return
    with open(path,'w',encoding='utf-8') as fp:
        content=content_replace(slist[0])
        fp.write(content)
        # for s in slist:
            # fp.write("%s\t\t%s\n" %(s[0].encode('utf8'),s[1].encode("utf8")))

def Page_Info(myPage):
    myPage_info=re.findall(r'<div class="bm_h cl">.*?<h2><a href="(.*?)" style="">(.*?)</a></h2>',myPage,re.S)
    return myPage_info


#获取一级页面的内容
def one_page_info(new_page):
    dom=etree.HTML(new_page)
    new_items=dom.xpath('//td/h2/a/text()')
    new_urls=dom.xpath('//td/h2/a/@href')
    assert (len(new_items))==len(new_urls)
    return zip(new_items,new_urls)

#获取二级页面的内容
def two_page_info(new_page):
    myPage_info=re.findall(r'<tbody id="normalthread_.*?">.*?<a class="tdpre y".*?>.*?<a href="thread-(.*?)".*?>(.*?)</a>',new_page,re.S)
    url=re.findall(r'</label><a href="(.*?)" class="nxt">.*?</a></div></span>',new_page,re.S)
    return myPage_info,url
    # dom=etree.HTML(new_page)
    # new_items=dom.xpath('//tr/th/a[-1]/text()')
    # new_urls=dom.xpath('//tr/th/a[-1]/@href')
    # assert (len(new_items))==len(new_urls)
    # return zip(new_items,new_urls)
# def get_next_page(new_page):
#     myPage_info=re.findall(r'<a href="(.*?)" class="nxt">',new_page,re.S)
#     return myPage_info

#获取具体页面内容
def get_page_info(new_page):
    myPage_info=re.findall(r'<td class="t_f".*?>(.*?)</td>',new_page,re.S)
    return myPage_info





def Spider(url):
    print("downloading",url)
    myPage=requests.get(url).content.decode('gbk')
    myPageResults=Page_Info(myPage)

    save_path=u'discuz'
    #获取首页的标题和连接
    for url,item in myPageResults:
        #不抓取关联技术专区
        if url!='forum.php?gid=165':
            url="http://www.discuz.net/"+url
            one_page=requests.get(url).content.decode('gbk')
            onePageResults=one_page_info(one_page)
            #进入一级页面，获取一级页面连接
            for one_item,one_url in onePageResults:
                #不抓取实验室，不抓取站长帮
                if one_url!='forum-3980-1.html' and one_url!='forum-flea-1.html' :
                    urllist=[one_url]
                    while urllist:
                        #获取二级页面内容
                        try:
                            two_page=requests.get("http://www.discuz.net/"+urllist[0]).content.decode('gbk')
                        except Exception as e:
                            print("获取列表页出错")
                            #如果报错，则直接解析下一页
                            print("http://www.discuz.net/"+urllist[0])
                            htmls=urllist[0].split("-")
                            num=htmls[2].split('.')
                            urllist[0]=re.sub('\d+',str(int(num[0])+1),urllist[0])
                            continue
                        #获取二级页面链接
                        twoPageResults,urllist=two_page_info(two_page)
                        # print urllist
                        #根据获取的连接，得到页面的具体内容
                        for two_url,two_item in twoPageResults:
                            two_path=os.path.join(save_path,item,one_item)
                            # save_path=save_path+'\\'+item+'\\'+one_item
                            url="http://www.discuz.net/thread-"+two_url
                            #获取页面的具体内容
                            try:
                                page=requests.get(url).content.decode('gbk')
                                pageResults=get_page_info(page)
                                filename=item_replace(two_item)
                                StringListSave(two_path,filename,pageResults)
                            except Exception as e:
                                print(e)
                                print('获取具体页面报错')
                                print(url)
                                continue


def item_replace(item):
    item=item.replace('/','')
    item=item.replace(u'\“','')
    item=item.replace(u'\”','')
    item=item.replace(u'【','')
    item=item.replace(u'】','')
    item=item.replace('|','')
    item=item.replace(u'?','')
    item=item.replace(':','')
    item=item.replace('//','')
    item=item.replace('*','')
    item=item.replace('<','')
    item=item.replace('>','')
    item=item.replace('\\','')
    return item

def content_replace(content):
    dr = re.compile(r'<[^>]+>',re.S)
    dd = dr.sub('',content)
    return dd

# def all_ticket_no_proxy():
#     start="start"
#     pool=mp.Pool(processes=5)
#     pool.map(Spider,start)
#     pool.close()
#     pool.join()


if __name__ == '__main__':
    print("Start")
    start_url="http://www.discuz.net/forum.php"
    Spider(start_url)
    # all_ticket_no_proxy()
    print("End")
