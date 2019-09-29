#有序字典
from collections import OrderedDict

#写入数据
from pyexcel_xls import save_data

def makeExcelFile(path, data):
    dic = OrderedDict()
    for sheetName, sheetValue in data.items():
        d = {}
        d[sheetName] = sheetValue
        dic.update(d)

    save_data(path, dic)

path = r"E:\python\office文件操作\4.excel操作\02.xls"
makeExcelFile(path, {"表一":[[1,2,3],[4,5,6],[7,8,8]],
                     "表二":[[11,21,31],[41,51,61],[71,81,81]]})