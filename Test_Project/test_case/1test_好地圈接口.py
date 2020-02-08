import unittest
import requests
from time import sleep
from file import data1

class HDQ_Api_Test(unittest.TestCase):
    def setUp(self):
        self.url=data1.url

    def test_土地详情页查看_massifDetail(self):
        body={"param":2}
        headers = {"Content-Type": "application/json","Cookie":data1.Cookie}
        r=requests.post(self.url+'/webclient/product/productType',json=body,headers=headers)
        result=r.json()
        print(result)

        self.assertEqual(result['status'],'200')
        self.assertEqual(result['message'],'请求成功')

        sleep(3)

    def test_回答删除_deteleAnswer(self):
        body = {"param": 2}
        headers = {"Content-Type": "application/json"}
        r = requests.post(self.url + '/webclient/question/deteleAnswer', json=body, headers=headers)
        result = r.json()
        print(result)

        self.assertEqual(result['status'], '2000')
        self.assertEqual(result['message'], '请求成功')

        sleep(3)



if __name__ == '__main__':
    unittest.main()
