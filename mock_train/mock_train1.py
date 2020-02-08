import unittest
from .modular import Count
class TestCount(unittest.TestCase):
    def test_add(self):
        count=Count()
        result=count.add2(8,5)
        print(result)
        self.assertEqual(result,13)

if __name__ == '__main__':
    unittest.main()