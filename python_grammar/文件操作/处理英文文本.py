path = r"E:\python\文件操作\Anna Karenina.txt"
path1 = r"E:\python\文件操作\test.txt"
f = open(path1,"wb")
#完整地读文件的过程
f1 = None
try:
    f1 = open(path,"r",encoding="utf-8")
    str = f1.read()
    str = str.replace(" ", "").lower()
    str = str.replace(",", "").replace(".", "").replace("?", "").replace("!", "").\
        replace(":", "").replace(";", "").replace("\n", "").replace("\t", "").replace("-", "").replace("&#39", "")
    print(str)
    f.write(str.decode("utf-8"))

    f.flush()
finally:
    if f1:
        f1.close()

        # 关闭文件时会刷新缓冲区,\n也刷新
    f.close()