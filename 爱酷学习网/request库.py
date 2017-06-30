# -*- coding: utf-8 -*-
import requests
#GET请求
# res = requests.get("http://cuiqingcai.com")
# print type(res)
# print res.status_code
# print res.encoding
# print res.cookies

#POST请求
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.post("http://httpbin.org/post", data=payload)
print r.text