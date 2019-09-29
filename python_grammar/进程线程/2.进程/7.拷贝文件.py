import os, time
from multiprocessing import Pool

#实现文件的拷贝
def copyFile(rPath, wPath):
    fr = open(rPath, "rb")
    fw = open(wPath, "wb")

    context = fr.read()
    fw.write(context)

    fr.close()
    fw.close()

rPath = ""
wPath = ""

#读取path下的所有文件
fileList = os.listdir(rPath)

#启动for循环处理每一个文件
start = time.time()
for fileName in fileList:
    copyFile(os.path.join(rPath, fileName), os.path.join(wPath, fileName))
end = time.time()
print("总耗时：%0.2f" % (end - start))