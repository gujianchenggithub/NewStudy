import unittest

class TestMath(unittest.TestCase):
    def setUp(self):
        print("test start....")
    def test_a(self):
        self.assertIs("11","11")
    def tearDown(self):
        print("test end.....")
if __name__ == '__main__':
    suite=unittest.TestSuite()
    suite.addTest(TestMath("test_a"))

    runer=unittest.TextTestRunner()
    runer.run(suite)