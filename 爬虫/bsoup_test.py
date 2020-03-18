import sys
from bs4 import BeautifulSoup

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
"""
soup=BeautifulSoup(html)
# print soup.prettify()
print("title:",soup.title)
print("head:",soup.head)
print("a:",soup.a)
print("p:",soup.p)
print("name:",soup.name)
print("head.name:",soup.head.name)
print("attrs:",soup.p.attrs)
soup.p['class']='newClass'
print(soup.p)
print(soup.p.string)
print(type(soup.p.string))

for child in soup.body.children:
    print(child)