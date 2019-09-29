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

if __name__ == "__main__":
    # 读取path下的所有文件
    fileList = os.listdir(rPath)
    start = time.time()

    pp = Pool(2)
    for fileName in fileList:
        pp.apply_async(copyFile, args=(os.path.join(rPath, fileName), os.path.join(wPath, fileName)))

        pp.close()
        pp.join()
        end = time.time()
        print("总耗时：%0.2f" % (end - start))