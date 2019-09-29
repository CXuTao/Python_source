"""

单元测试：

作用：用来对一个函数，一个
类或者一个模块来进行正确性校验
工作

结果：
1.单元测试通过，说明我们测试的函数功能正常
2.单元测试不通过，说明函数功能有BUG，
要么测试条件输入有误

"""

def mySun(x, y):
    #return x + y + 1
    return x + y
def mySub(x, y):
    return x - y

print(mySun(1,3))
