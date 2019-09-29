import win32com
import win32com.client

def makePPT(path):
    ppt = win32com.client.Dispatch("PowerPoint.Application")
    ppt.Visible = True

    #增加一个文件
    pptFile = ppt.Presentations.Add()

    #创建页
    #参数一为页数（从一开始）参数二为类型
    page1 = pptFile.Slides.Add(1,1)
    t1 = page1.Shapes[0].TextFrame.TextRange
    t1.Text = "xt is a good man"
    t2 = page1.Shapes[1].TextFrame.TextRange
    t2.Text = "xt is a good man"

    #第二页
    page2 = pptFile.Slides.Add(2, 1)
    t3 = page2.Shapes[0].TextFrame.TextRange
    t3.Text = "xt is a good man"
    t4 = page2.Shapes[1].TextFrame.TextRange
    t4.Text = "xt is a good man"

    # 第三页
    page3 = pptFile.Slides.Add(3, 2)
    t5 = page3.Shapes[0].TextFrame.TextRange
    t5.Text = "xt is a good man"
    t6 = page3.Shapes[1].TextFrame.TextRange
    t6.Text = "xt is a good man"

    #保存
    pptFile.SaveAs(path)
    pptFile.Close()
    ppt.Application.Quit()

path = r"E:\python\office文件操作\5.写ppt\01.ppt"
makePPT(path)