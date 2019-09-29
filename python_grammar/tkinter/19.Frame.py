import tkinter

#创建主窗口
win = tkinter.Tk()
#设置标题
win.title("哈哈哈")
#设置大小和位置
win.geometry("400x400+200+20")

"""
框架控件
在屏幕上显示一个矩形区，多为容器控件
"""
frm = tkinter.Frame(win)
frm.pack()

#left
frm_1 = tkinter.Frame(frm)
tkinter.Label(frm_1, text="左上", bg="pink").pack(side=tkinter.TOP)
tkinter.Label(frm_1, text="左下", bg="blue").pack(side=tkinter.TOP)
frm_1.pack(side=tkinter.LEFT)

#left
frm_r = tkinter.Frame(frm)
tkinter.Label(frm_r, text="右上", bg="red").pack(side=tkinter.TOP)
tkinter.Label(frm_r, text="右下", bg="yellow").pack(side=tkinter.TOP)
frm_r.pack(side=tkinter.RIGHT)

win.mainloop()