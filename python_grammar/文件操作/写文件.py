import time

path = r"E:\python\test1.txt"
f = open(path,"w")

#1.将信息写入缓冲区
f.write("hello world")
#2.刷新缓冲区
#直接把缓冲区的内容写入文件
f.flush()

while True:
    f.write("hello world")
    f.flush()
    time.sleep(0.1)

#关闭文件时会刷新缓冲区,\n也刷新
f.close()