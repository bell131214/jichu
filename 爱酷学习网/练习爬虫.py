# -*- coding: utf-8 -*-

#下载贴吧或空间所有图片
import re
import urllib2

def getHtml(url):
    page = urllib2.urlopen(url)
    html = page.read()
    return html
def getImg(html):
    reg = r'src="(.*?\.jpg)"width'
    imgre = re.compile(reg)
    imgList = re.findall(imgre,html)
    return imgList
html = getHtml("http://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&word=%E6%A1%8C%E9%9D%A2")
print getImg(html)
