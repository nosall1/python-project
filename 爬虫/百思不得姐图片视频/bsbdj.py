#-*- coding:utf-8 -*-
import os,requests,bs4
print('百思不得姐……')
url='http://www.budejie.com/detail-30183671.html'
os.makedirs('bsbdj',exist_ok=True)
statusValue=True
while statusValue:
    # 下载网页
    print('Downloading page %s ...'%url)
    result=requests.get(url)
    soup=bs4.BeautifulSoup(result.text,'html.parser')
    # 查找图像
    imgs=soup.select(".j-r-list-c-img")
    if imgs==[]:
        print('Could not find img')
        break
    else:
        imgUrl=(imgs[0].contents)[1].attrs['src']
        print('Downloading image %s...'%imgUrl)
        res=requests.get(imgUrl)
        imageFile=open(os.path.join('bsbdj',os.path.basename(imgUrl)),'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
    nextLink=soup.select('.c-next-btn')[0]
    url='http://www.budejie.com'+nextLink.get('href')

print('Done')