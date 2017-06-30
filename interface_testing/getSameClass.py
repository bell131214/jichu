# coding=utf-8
import requests

def TEST_1():
    header = {
        "Content-Type":  "text/html"
    }
    payload = {"day":"2016-12-09",
               "numberTeacher":"1",
               "applyTechBId":"7",
               "applyClassId":"108",
               "selectUnitApply":"5",
               "applyType":"D"

    }
    url = "http://192.168.101.172:7071/deansCourse/api/getSameClassAndDeptAndSubjectTeacher"
    res = requests.post(url,data=payload)
    print res.url
    print res.text
# 空指针错误
if __name__=='__main__':
    TEST_1()