#支持包
"""
pip install --index https://mirrors.ustc.edu.cn/pypi/web/simple/ xlrd

pip install --index https://mirrors.ustc.edu.cn/pypi/web/simple/ future

pip install --index https://mirrors.ustc.edu.cn/pypi/web/simple/ xlwt-future

pip install --index https://mirrors.ustc.edu.cn/pypi/web/simple/ pyexcel-io

pip install --index https://mirrors.ustc.edu.cn/pypi/web/simple/ ordereddict

pip install --index https://mirrors.ustc.edu.cn/pypi/web/simple/ pyexcel

pip install --index https://mirrors.ustc.edu.cn/pypi/web/simple/ pyexcel-xls
"""

#有序字典
from collections import OrderedDict

#读取数据
from pyexcel_xls import get_data

def readXlsAndXlsxFile(path):
    dic = OrderedDict()

    #抓取数据
    xdata = get_data(path)

    for sheet in xdata:
        dic[sheet] = xdata[sheet]
    return dic

path = r"E:\python\office文件操作\4.excel操作\01.xls"
dic = readXlsAndXlsxFile(path)
print(dic)
print(len(dic))