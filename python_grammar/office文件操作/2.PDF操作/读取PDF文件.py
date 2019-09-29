import sys
import importlib
importlib.reload(sys)

from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal, LAParams
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed

def readPDF(path, toPath):
    #以二进制形式打开pdf文件
    f = open(path, "rb")
    #创建一个pdf文件分析器
    parser = PDFParser(f)
    #创建pdf文档
    pdfFile = PDFDocument()
    #链接分析器与文档对象
    parser.set_document(pdfFile)
    pdfFile.set_parser(parser)
    #提供初始化密码
    pdfFile.initialize()
    #检测文档是否提供txt转换
    if not pdfFile.is_extractable:
        #raise PDFTextExtractionNotAllowed
        None
    else:
        #解析数据
        #数据管理器
        manager = PDFResourceManager()
        #创建一个PDF设备管理器
        laparams = LAParams()
        device = PDFPageAggregator(manager, laparams=laparams)
        #解释器对象
        interpreter = PDFPageInterpreter(manager, device)

        #开始循环处理
        for page in pdfFile.get_pages():
            interpreter.process_page(page)
            layout = device.get_result()
            for x in layout:
                if (isinstance(x, LTTextBoxHorizontal)):
                    with open(toPath, "a") as f:
                        str = x.get_text()
                        print(str)
                        f.write(str+"\n")

path = r"E:\python\office文件操作\2.PDF操作\2017级班级课表(1).pdf"
toPath = r"E:\python\office文件操作\2.PDF操作\05.txt"
readPDF(path, toPath)
