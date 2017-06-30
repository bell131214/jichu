# coding=utf-8
# 加载模块
import httplib,urllib
import unittest

# 定义类
class UserInfoTests(unittest.TestCase):
    def setUp(self):
        # 与服务器建立一个连接
        self.conn = httplib.HTTPConnection("192.168.101.172:7071")
        # 定义文件头
        self.headers = {"Accept":"text/html"}
        # 定义发送的数据参数
        self.params = urllib.urlencode({"now":"1480756183924","flag":"3",
        "semester":"20161",
        "techName": "李坚",
        "teacherId": "df7460a3 - 9680 - 431d - bd2a - d860d1f3ac0f"
    })
        # 开始数据提交，提示也可以使用get进行
        self.conn.request(method="get",url="http://192.168.101.172:7071/deansCourse/api/getCourseSchedule",
                          body=self.params,headers=self.headers)
        # 处理返回后的数据
        self.response = self.conn.getresponse()
    def test_name(self):
        self.a = self.response.read()

    def tearDown(self):
        self.conn.close()

if __name__=='__main__':
    unittest.main(verbosity=2)





