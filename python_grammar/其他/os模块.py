import os
"""
os:包含了普遍操作系统的功能

"""
#获取操作系统的类型 nt->windows posix->Linux/Unix/Mac
print(os.name)

#打印操作系统详细信息，windows操作系统不支持
#print(os.uname())

#获取操作系统中的环境变量
print(os.environ)
#获取指定环境变量
os.environ.get("APPDATA")
#获取当前目录
print(os.curdir)
#获取当前的工作目录，及当前python脚本所在目录
print(os.getcwd())
#返回当前目录下的所有文件
print(os.listdir( r"E:\python"))
#在当前目录下创建新目录，参数为路径
os.mkdir("xutao")
#删除目录
os.rmdir("xutao")
#获取文件属性
print(os.stat("test.txt"))
#重命名
#os.rename("hhh","test1.txt")
#删除文件
#os.remove("test1.txt")
#运行shell命令,就是运行命令行的命令
#os.system("notepad")
#os.system("write")
#os.system("mspaint")
#os.system("msconfig")
#os.system("shutdown -s -t 500")
#os.system("shutdown -a")
#os.system("taskkill /f /im QQ.exe")


#有些方法存在与os模块里，还有些方法存在于os.path
#查看当前的绝对路径
print(os.path.abspath(""))

#拼接路径
p1 = r"E:\python\test2.txt"
p2 = "hhh"
#注意参数二开始不能有斜杠
print(os.path.join(p1,p2))

#拆分路径
path =r"C:\gdhj\jdnvjk\jdkvnjfdk"
print(os.path.split(path))

#获取扩展名
print(os.path.splitext(path))

#判断是否是目录
print(os.path.isdir(path))

#判断文件是否存在
print(os.path.isfile(path))

#判断目录是否存在
print(os.path.exists(path))

#获得文件的大小（字节）
print(os.path.getsize(r"E:\python\test.txt"))

#获取文件目录
print(os.path.dirname(path))
#获取文件名
print(os.path.basename(path))

