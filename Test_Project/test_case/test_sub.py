from calculator import *
from StartEnd import *

class Test_sub(Setup_tearDown):

    def test_sub(self):
        i=Math(15,5)
        self.assertEqual(i.sub(),110)


    def test_sub1(self):
        i=Math(5,8)
        self.assertEqual(i.sub(),-3)
