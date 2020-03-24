#-*- coding:utf-8 -*-
from bs4 import BeautifulSoup
from selenium import webdriver
def main():
    driver=webdriver.Chrome()
    driver.get('https://v.taobao.com/v/content/live?catetype=704&from=taonvlang')
    soup=BeautifulSoup(driver.page_source,'html.parser')
    for img_tag in soup.body.select('img[src]'):
        print(img_tag.attrs['src'])

if __name__ == '__main__':
    main()
