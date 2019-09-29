"""
递归调用：一个函数，调用了自身，成为递归调用

凡是循环能干的事，递归都能干
"""

"""
方式：
1、写出临界条件
2、找这一次和上一次的关系
3、假设当前函数已经能用，调用自身计算上一次的结果，再求出本次的结果
"""

#输入一个数（大于1），求1+2+...+n的和
def sum1(n):
    sum = 0
    for x in range(1,n + 1):
        sum += x
    return sum

print(sum1(9))

def sum2(n):
    if n == 1:
        return 1
    else:
        return sum2(n - 1) + n

print(sum2(9))
