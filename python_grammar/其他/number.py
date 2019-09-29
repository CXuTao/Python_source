import math
import  random
'''
分类：整数、浮点数、复数

'''

'''
整数：Python可以处理任意大小的整数
'''

num1 = 10

#连续定义多个变量
num2 = num3 = num4 = 11
print(id(num2))
print(id(num3))
#交互式赋值定义变量
num5,num6 = 6,7

print(int(1.1))
print(int(1.9))

#函数
a1 = -10
a2 = abs(a1)
print(a2)

#比较两个数的大小
a3 = 100
a4 = 9
print((a3>a4)-(a3<a4))

#返回两数的最大值
print(max(1,12,34,55,67))

print(min(56,3243,546,898,76))

print(pow(2,5))

print(round(3.456))
print(round(3,567))
print(round(3.456,2))
print(round(3.546,1))

#下面的函数需要库
#向上取整
print(math.ceil(18.1))
#向下取整
print(math.floor(18.1))
#返回小数部分和整数部分
print(math.modf(22.3))
#开方
print(math.sqrt(12))

#随机数出列表中的一个数或字符串
print(random.choice([1,3,5,7,5,8,27]))
print(random.choice(range(5)))
print(random.choice("hello"))

r1 = random.choice(range(10)) + 1
#产生随机奇数
print(random.randrange(1,100,2))
#0-99
print(random.randrange(100))
#0-1
print(random.randrange())

list = [1,2,3,4,5]
#将列表的所有元素随机排序
random.shuffle(list)
print(list)
#随机生成一个实数
print(random.uniform(3,9))

print(1 + 1)
print(1 ** 1)
print(1 / 1)
print(1 // 1)
