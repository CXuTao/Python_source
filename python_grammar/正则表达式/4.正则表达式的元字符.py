import re



print("________________匹配单个字符与数字_________")
"""
.                            匹配除换行符以外的任意字符
[0123456789]                 匹配方括号中所包含的任意一个字符 []是字符集合
[abcdefghijklmnopqrstuvwxyz] 匹配单个字母
[a-z]                        匹配任意小写字母
[A-Z]
[0-9]
[0-9a-zA-Z]                  匹配任意数字、字母
[0-9a-zA-Z_]                 匹配任意数字、字母和下划线
[^asd]                       匹配除了asd这几个字母以外的所有字符,^称为脱字符，表示不匹配集合中的字符
[^0-9]                       匹配所有非数字字符
\d                           匹配数字，效果和[0-9]一样
[^\d]
\D                           匹配非数字字符
\w                           匹配数字、字母和下划线
\W                           匹配非数字、字母和下划线
\s                           匹配任意的空白符（空格、换行、回车、换页、制表）效果同[ \f\n\r\t]
\S                           匹配任意的非空白符（空格、换行、回车、换页、制表）效果同[^ \f\n\r\t]


"""

print(re.search(".", "xutao"))


print("________________锚字符（边界字符）_____________")
"""
^      行首匹配，和在中括号里面的不是一个意思
$      行尾匹配
\A     匹配字符串开始，它和^的区别是，\A只匹配整个字符串的开头，即使在re.M的模式下也不会匹配其他行的行首
\Z     匹配字符串结束，它和$的区别是，\Z只匹配整个字符串的结尾，即使在re.M的模式下也不会匹配其他行的行尾
\b     匹配一个单词的边界，也就是单词和空格间的位置
       "er\b"可以匹配never不能匹配nerve
\B     匹配非单词边界
"""

print(re.findall("\Axutao", "xutao is\n xutao is", re.M))
print(re.findall("^xutao", "xutao is\nxutao is", re.M))
print(re.search(r"er\b", "never"))
print(re.search(r"er\b","nerve"))
print(re.search(r"er\B", "never"))
print(re.search(r"er\B","nerve"))


print("_____________匹配多个字符_____________")

"""

说明：下方的x、y、z、n、m均为普通字符，不是正则表达式的元字符
(xyz)       匹配小括号内的xyz(作为一个整体去匹配)
x?          匹配0个或者是1个x
x*          匹配0个或者是任意多个x(.*表示匹配0个或者任意多个字符（换行符除外））
x+          匹配至少一个x
x{n}        匹配确定的n个x（n是一个非负整数）
x{n,}       匹配至少n个x
x{n,m}    匹配至少n个最多m个x  注意n<=m
x|y         |表示或，匹配x或y



"""

print(re.findall(r"(xutao)", "xutaois a good man, xutao is a"))
print(re.findall(r"a?", "aaa"))#非贪婪匹配（尽可能少的匹配）
print(re.findall(r"a*", "aaabaa"))#贪婪匹配（尽可能多的匹配）
print(re.findall(r"a+", "aaabaa"))#贪婪匹配（尽可能多的匹配）
print(re.findall(r"((x|Xutao))", "xutao---Xutao"))



print("______________________特殊________________")
"""
*? +? x? 最小匹配 通常都是尽可能多的匹配，可以使用这种方式解决贪婪匹配
(?:x)    类似(xyz)，但不表示一个组

"""
print(re.findall(r"//*.*?/*/", "/* efreterg */ /* rhethjuryu */"))


