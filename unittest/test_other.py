import unittest
class test1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("class start test>>>>>>>>>>>>>>>>>>>>>>>>>>>>")


    @classmethod
    def tearDownClass(cls):
        print("class end test>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

    def setUp(self):
        print("test1 start...")


    def test_a(self):
        print("test_a...")


    def test_b(self):
        print("test_b...")

    def tearDown(self):
        print("test1 end....")

class test2(unittest.TestCase):


    @classmethod
    def setUpClass(cls):
        print("class start test>>>>>>>>>>>>>>>>>>>>>>>>>>>>")


    @classmethod
    def tearDownClass(cls):
        print("class end test>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

    def setUp(self):
        print("test2 start....")

    def test_c(self):
        print("test_c")


    def test_d(self):
        print("test d")

    def tearDown(self):
        print("test2 end......")

if __name__ == '__main__':
    unittest.main()