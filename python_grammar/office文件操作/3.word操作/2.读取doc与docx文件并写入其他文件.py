import win32com
import win32com.client

def readWordFileToOtherFile(path, toPath):
    mw = win32com.client.Dispatch("Word.Application")
    doc = mw.Documents.Open(path)

    #将word的数据保存到另一个文件
    doc.SaveAs(toPath, 2)#2表示为txt文件

    #关闭文件
    doc.Close()
    #退出word
    mw.Quit()


path = r"E:\python\office文件操作\3.word操作\01.doc"
toPath = r"E:\python\office文件操作\3.word操作\01.txt"
readWordFileToOtherFile(path, toPath)