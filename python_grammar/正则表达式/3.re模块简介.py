import re

"""
re.match函数
原型：match(pattern, string, flags=0)
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
功能：尝试从字符串的起始位置匹配一个模式
如果不是起始位置匹配成功的话，返回None
"""


#www.baidu.com
print(re.match("www", "www.baidu.com"))
print(re.match("www", "ww.baidu.com"))
print(re.match("www", "baiduwww.com"))
print(re.match("www", "wwW.baidu.com", flags=re.I).span())
#扫描整个字符串，返回从起始位置成功匹配的

"""

re.search函数
原型：search(pattern, string, flags=0)
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
功能：扫描整个字符串，并返回第一个成功的匹配（不必只能从头开始）

"""

print(re.search("hhh",  "wqdwfvffdfvdhhhkljlkhhh"))

"""
re.findall函数
原型：findall(pattern, string, flags=0)
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
功能：扫描整个字符串，并返回结果列表

"""

print(re.findall("hhh",  "wqdwfvffdfvdhhhhhkljlkhhh"))





