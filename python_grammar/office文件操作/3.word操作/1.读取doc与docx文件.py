import win32com
import win32com.client

def readWordFile(path):
    #调用系统word功能，可以处理doc和docx两种文件
    mw = win32com.client.Dispatch("Word.Application")
    #打开文件
    doc = mw.Documents.Open(path)
    for paragraphs in doc.Paragraphs:
        line = paragraphs.Range.Text
        print(line)
    #关闭文件
    doc.Close()
    #退出word
    mw.Quit()

path = r"E:\python\office文件操作\3.word操作\01.doc"
readWordFile(path)