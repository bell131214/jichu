# -*- coding: utf-8 -*-
import urllib2
import urllib
# def gethtml(url):
#     page = urllib2.urlopen(url)
#     html = page.read()
#     return html
# # def getimage(html):
# #     r = ""
# print gethtml("http://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&word=%E6%A1%8C%E9%9D%A2")

# page = urllib2.urlopen('http://www.baidu.com')
# html = page.read()
# print html

#构造一个request
# url = 'http://www.baidu.com'
# request = urllib2.Request(url)
# page = urllib2.urlopen(request)
# html = page.read()
# print html
import urllib2
import urllib
#GET方式
# url = 'http://www.baidu.com'
# values = {}
# values['username']='python'
# values['password']='xxxx'
# data = urllib.urlencode(values)
# geturl = url+"?"+data
# print geturl
# request = urllib2.Request(geturl)
# page = urllib2.urlopen(request)
# html = page.read()
# print html
#POST方式
# url = 'http://www.baidu.com'
# values = {'username':'xxx','password':123456}
# data = urllib.urlencode(values)
# request = urllib2.Request(url,data)
# page = urllib2.urlopen(request)
# html = page.read()
# print html

#异常的处理
# import urllib2
# request = urllib2.Request('http://www.xxx.com')
# try:
#     urllib2.urlopen(request)
# # except urllib2.URLError as e:
# except urllib2.URLError ,e: #和上面是一个意思
#     print e.reason
#HTTPError的异常
request = urllib2.Request('http://blog.csdn.net/cqcre')
try:
    urllib2.urlopen(request)
except urllib2.HTTPError,e:
    print e.code
    print e.reason

#设置cookie
import urllib2
import cookielib

