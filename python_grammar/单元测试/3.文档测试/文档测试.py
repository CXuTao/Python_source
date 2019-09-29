import doctest
#这个模块可以提取注释中的代码执行
#doctest严格按照Python交互模式的输入提取



def mySun(x, y):
    """
    get the sum from x and y
    :param x: firstNum
    :param y: secounNum
    :return: sum

    example:
    >>> print(mySun(1,2))
    3

    """
    #写文档注释要注意格式，>>>后面有一个空格
    #return x + y + 1
    return x + y

print(mySun(1,2))

#进行文档测试
doctest.testmod()










