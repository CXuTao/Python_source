import unittest
from 对函数进行单元测试 import  mySun
from 对函数进行单元测试 import  mySub

class Test(unittest.TestCase):
    def setUp(self):
        print("开始测试时自动调用")
    def tearDown(self):
        print("结束测试时自动调用")

    #为了测试mySum
    def test_mySun(self):
        self.assertEqual(mySun(1,2), 3, "加法有误")

    def test_mySub(self):
        self.assertEqual(mySub(2, 1), 1, "减法有误")

if __name__ == "__main__":
    unittest.main()
