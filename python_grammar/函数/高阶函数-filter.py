"""

filter(fn. lsd)
参数一为函数
参数二为序列

功能：用于过滤序列
就是把传入的函数依次作
用于序列的每个元素，根据返回的
是True还是False决定是否保留该元素

"""

list1 = [1,2,3,4,5,6]
#筛选条件
def func(num):
    #偶数保留
    if num%2 == 0:
        return True
    #奇数剔除
    return False
l = filter(func, list1)
print(list(l))
print(list1)