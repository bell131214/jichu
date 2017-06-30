# coding=utf-8
import requests

def TEST_1():
    header = {
        "Content-Type":  "text/html"
    }
    params = {
        "DeptID":"1480934176927"
    }
    url = "http://192.168.101.172:7071/deansCourse/api/getStuClassList"
    res = requests.get(url,params=params)
    print res.url
    print res.text

if __name__=='__main__':
    TEST_1()