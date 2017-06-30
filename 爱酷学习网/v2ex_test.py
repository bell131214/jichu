# -*- coding: utf-8 -*-
import unittest
import requests

class V2EXTestCase(unittest.TestCase):

    def test_get_node_api(self):
        python_node_id = 90
        url = "https://www.v2ex.com/api/nodes/show.json"
        node_name = 'python'
        querystring = {"name":node_name}
        res = requests.request("GET", url, params=querystring).json()
        print(res)
        self.assertEqual(res['id'], python_node_id)
        self.assertEqual(res['name'], node_name)

if __name__ == '__main__':
    unittest.main()
