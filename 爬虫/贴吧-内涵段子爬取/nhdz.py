#-*- coding:utf-8 -*-
# 写入文件
import requests,os,bs4


def write_file(file_url,file_type):
    res=requests.get(file_url)
    res.raise_for_status()
    # 文件类型分文件夹写入
    if file_type==1:
        file_folder=os.path.join('nhbz','jpg')
    elif file_type==2:
        file_folder=os.path.join('nhbz','mp4')
    else:
        file_folder=os.path.join('nhbz','other')

    if not os.path.exists(file_folder):
        os.makedirs(file_folder,exist_ok=True)

    file_name=os.path.basename(file_url)
    str_index=file_name.find('?')

    if str_index>0:
        file_name=file_name[:str_index]

    file_path=os.path.join(file_folder,file_name)
    print('正在写入资源文件：',file_path)
    image_file=open(file_path,'wb')
    for chunk in res.iter_content(100000):
        image_file.write(chunk)
    image_file.close()
    print('写入完成！')

# 获取资源的url
def download_file(web_url):
    print('正在下载网页：%s...'%web_url)
    result=requests.get(web_url)
    soup=bs4.BeautifulSoup(result.text,'html.parser')
    # 查找图片资源
    img_list=soup.select('.vpic_wrap img')
    if img_list==[]:
        print("未发现图片资源")
    else:
        for img_info in img_list:
            file_url=img_info.get('bpic')
            write_file(file_url,1)

    #查找视频资源
    video_list=soup.select(".threadlist_video a")
    if video_list==[]:
        print('未找到视频资源')
    else:
        for video_info in video_list:
            file_url=video_info.get('data-video')
            write_file(file_url,2)
    print('下载资源结束：',web_url)
    next_link=soup.select("#frs_list_pager .next")
    if next_link==[]:
        print('下载资源结束')
    else:
        url=next_link[0].get('href')
        download_file("https"+url)

if __name__ == '__main__':
    web_url='https://tieba.baidu.com/f?ie=utf-8&kw=段友之家'
    download_file(web_url)