import  time
"""
UTC(世界协调时间)：格林尼治时间，世界标准时间
在中国来说是UTC+8
DST(夏令时)：是一种节约能源而人为规定时间制度，
在夏季调快1个小时

事件表现形式：
1、时间戳
以整形或浮点型表示时间的一个以秒为时间间隔，这个时间间隔的基础值
是从1970年1月1日凌晨开始算起的
2、元组
一种python的数据结构表示，这个元祖有9个模型内容
year
day
hours
minutes
seconds
weekday
Julia day
flag   (1 或 -1 或 0)
3、格式化字符串

"""
#返回当前时间的时间戳，浮点数形式，不需要参数
c = time.time()
print(c)

#将时间戳转为UTC时间元组
t = time.gmtime(c)
print(t)

#将时间戳转为本地时间元组
b = time.localtime(c)
print(b)

#将本地时间元组转化为时间戳
m = time.mktime(b)
print(m)

#将时间元组转成字符串
s = time.asctime()
print(s)

#将时间戳转为字符串
p = time.ctime(c)
print(p)

#将时间元组转换成给定格式的字符串，参数二维时间元组，参数二不存在，认为转化当前时间
q = time.strftime("%Y-%m-%d %H:%M:%S",b)
print(q)
print(type(q))

#将时间字符串转为时间元组
w = time.strptime(q,"%Y-%m-%d %H:%M:%S")
print(w)

#延迟时间
time.sleep(1)

#返回当前程序的cpu执行时间
#UNIX系统始终返回全部的运行时间
#windows从第二次开始，都是以第一个调用此函数的
#开始时间戳作为基数
y1 = time.clock()
print("%d" % y1)
time.sleep(1)
y2 = time.clock()
print("%d" % y2)
time.sleep(2)
y3 = time.clock()
print("%d" % y3)