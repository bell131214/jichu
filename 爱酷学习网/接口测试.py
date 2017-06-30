# -*- coding: utf-8 -*-
import requests
import unittest
class V2EXTestCase(unittest.TestCase):

    def test_get_node_api(self):
        python_node_id = 90
        url = "https://www.v2ex.com/api/nodes/show.json"
        node_name = 'python'
        querystring = {"name":node_name}
        res = requests.request("GET", url, params=querystring).json()#JSON 解码器,不然断言会失败
        print(res)
        self.assertEqual(res['id'], python_node_id)
        self.assertEqual(res['name'], node_name)

#代码重构，把所有重复的参数替换
if __name__=='__main__':
    unittest.main()
#
# import requests
# url = "https://www.v2ex.com/api/nodes/show.json"
# querystring = {"name":"python"}
# headers = {
#     'cache-control': "no-cache",
#     'postman-token': "d4573b10-8c5d-f199-673c-4eb8185fca88"
#     }
# response = requests.request("GET", url, headers=headers, params=querystring)
#
# print(response.text)


