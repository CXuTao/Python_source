import re


"""

字符串切割

"""
str1 = "xutao      is a good man"
print(str1.split(" "))
print(re.split(r" +", str1))


"""

re.finditer()函数
原型：finditer(pattern, string, flags=0)
参数：
patter:模式匹配的正则表达式
string:要匹配的字符串
flags:标志位，用于控制正则表达式的匹配方式
re.I  忽略大小写
re.L  做本地化识别
re.M  多行匹配，影响^和$
re.S  使.匹配包括换行符在内的所有字符
re.U  根据Unicode字符集解析字符，影响\w \W \b \B
re.X  使我们灵活的理解正则表达式
功能：与findall类似，扫描整个字符串，返回一个迭代器

"""

str2 = "xutao is a good man! xutao is a nice man"
d = re.finditer(r"(xutao)", str2)
while True:
    try:
        print(next(d))
    except StopIteration as e:
        break


"""

字符串的替换和修改
sub(pattern, repl, string, count=0, flags=0)
subn(pattern, repl, string, count=0, flags=0)
pattern:    正则表达式（规则）
repl:       指定的用来替换的字符串
string:     目标字符串
count:      最多替换次数
功能：在目标字符串中以正则表达式的规则匹配字符串，
再把他们替换成指定的字符串，可以制定替换的次数，
如果不知道，替换所有的匹配字符串

区别：返回类型不同，前者返回一个被替换的字符串，后者返回一个元组
第一个元素为一个被替换的字符串，第二个元素为替换次数

"""

str3 = "xutao is a good good good man"
print(re.sub(r"(good)", "nice",str3))
print(re.subn(r"(good)", "nice",str3))



"""

分组：
概念：除了简单的判断是否匹配之外，正则表达式还有提取子串的功能。
用（）表示的就是提取出来的分组

"""

str4 = "010-53247654"
m = re.match(r"(?P<first>\d{3})-(?P<last>\d{8})", str4)
n = re.match(r"((\d{3})-(\d{8}))", str4)
#使用序号获取对应组的信息，group(0)一直代表原始字符串
print(m.group(0))
print(m.group(1))
#根据给组起的名字获取组
print(m.group("first"))
print(m.group(2))
#查看匹配的各组的情况
print(m.groups())


"""

编译：当我们使用正则表达式时re模块会干两件事
1、编译正则表达式，如果正则表达式本身不合法，会报错
2、用编译后的正则表达式去匹配对象
compile(pattern, flags=0)
pattern：要编译的正则表达式

"""

pat = r"^1(([3578]\d)|(47))\d{8}$"
print(re.match(pat, "13610603393"))
#编译为正则对象
re_telephone = re.compile(pat)
print(re_telephone.match("13610603393"))

"""

QQ:

"""
re_QQ = re.compile(r"^[1-9]\d{5,9}$")
print(re_QQ.search("1234567890"))