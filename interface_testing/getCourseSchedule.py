# coding=utf-8
import requests

def TEST_1():
    header = {
        "Content-Type":  "text/html"
    }
    params = {"now":"1480906415069",
        "flag":"3",
        "semester":"20161",
        "techName": "%E6%9D%8E%E5%9D%9",
        "teacher": "df7460a3 - 9680 - 431d - bd2a - d860d1f3ac0f"
    }
    # url = "http://192.168.101.172:7071/deansCourse/scheduling/queryClassCourseScheduledTable"
    url = "http://192.168.101.172:7071/deansCourse/api/getCourseSchedule"
    res = requests.get(url,params=params)
    print res.url
    print res.text
if __name__=='__main__':
    TEST_1()

