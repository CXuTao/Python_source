"""
1.打开文件
2.读文件内容
3.关闭文件
"""

"""
1.打开文件
open(path,flag,encoding)
flag:打开方式
r    只读，文件指针在文件开头
rb   二进制形式打开文件，只读，文件指针在文件开头
r+   打开一个文件，可读写，文件指针在文件开头
w    写文件，文件指针在文件开头，会覆盖文件
wb   写入二进制值
w+   读写
a    追加，文件指针在末尾
a+   
encoding:编码方式
errors:错误处理
"""

path = r"E:\python\test.txt"
f = open(path,"r",encoding="utf-8",errors="ignore")


"""
2.读文件
"""
#1.读文件全部内容
str1 = f.read()
print(str1)
#读完以后文件指针在末尾
f.seek(0)
#2.读取指定字符数
str2 = f.read(10)
print(str2)
f.seek(0)
#3.读取整行包括换行
str3 = f.readline()
f.seek(0)
#4.读取指定字符数
str4 = f.readline(10)
f.seek(0)
#5.读取所有行返回列表
str5 = f.readlines()
f.seek(0)
#6.若给定数字大于0，返回实际字节的行数
str6 = f.readlines(20)
f.seek(0)
#修改文件指针的位置
f.seek(0)
"""
3.关闭文件
"""
f.close()

#完整地读文件的过程
try:
    f1 = open(path,"r",encoding="utf-8")
    print(f1.read())
finally:
    if f1:
        f1.close()

#可以自动关闭文件
with open(path,"r",encoding="utf-8") as f2:
    print(f2.read())
    