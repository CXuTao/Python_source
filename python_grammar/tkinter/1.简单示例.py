import tkinter

#创建主窗口
win = tkinter.Tk()
#设置标题
win.title("哈哈哈")
#设置大小和位置
win.geometry("400x400+200+20")


#进入消息循环
"""
列表框控件，可以包含一个或多个文本框
作用：可以在listbox控件的小窗口显示一个字符串
"""

#1.创建一个listbox,添加几个元素

#MULTIPLE支持多选
lb = tkinter.Listbox(win, selectmode=tkinter.MULTIPLE)
for item in ["good", "nice", "handsome", "vg", "vn"]:
    #按顺序添加
    lb.insert(tkinter.END, item)

lb.pack()

win.mainloop()