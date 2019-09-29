import csv

def readCsv(path):
    infoList = []
    with open(path, "r") as f:
        allFileInfo = csv.reader(f)
        for row in allFileInfo:
            infoList.append(row)
    return infoList



path = r"E:\python\office文件操作\1.读写CSV文件\12.csv"
readCsv(path)