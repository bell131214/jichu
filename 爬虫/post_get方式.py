# -*- coding: utf-8 -*-

#post方式
import urllib2
import urllib

values = {"username":"110100@qq.com","password":"xxx"}
data = urllib.urlencode(values)
user_agent = "Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)"
headers = {"User-Agent" : user_agent,   'Referer':'http://www.zhihu.com/articles'}
url = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
#构造一个request
request = urllib2.Request(url,data,headers)
response = urllib2.urlopen(request)
print response.read()

#get方式
import urllib2
import urllib
values = {"username":"110100@qq.com","password":"xxx"}
data = urllib.urlencode(values)
url = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
geturl = url+"?"+data
request = urllib2.Request(geturl)
response = urllib2.urlopen(request)
print response.read()

#proxy代理的设置
import urllib2
enable_proxy = True
proxy_handler = urllib2.ProxyHandler({"http" : 'http://some-proxy.com:8080'})
null_proxy_handler = urllib2.ProxyHandler({})
if enable_proxy:
    opener = urllib2.build_opener(proxy_handler)
else:
    opener = urllib2.build_opener(null_proxy_handler)
urllib2.install_opener(opener)

#URLError
import urllib2

request = urllib2.Request("http://blog.csdn.net/cqcre")
try:
    urllib2.urlopen(request)
except urllib2.HTTPError,e:
    print e.code
except urllib2.URLError,e:
    print e.reason
else:
    print "ok"
