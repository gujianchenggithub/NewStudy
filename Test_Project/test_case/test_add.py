from calculator import *
from StartEnd import *
import unittest
from operateDB import operateDb

class Test_add(Setup_tearDown):

    @unittest.skip("我手动设置失败的de 。。。。。")

    def test_add(self):
        j=Math(5,5)
        self.assertEqual(j.add(),110)


    def test_add1(self):
        j=Math(5,8)
        self.assertEqual(j.add(),13)

