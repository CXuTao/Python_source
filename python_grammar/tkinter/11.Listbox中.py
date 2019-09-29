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
#绑定变量
lbv = tkinter.StringVar()
#与BORWSE相似，但是不支持鼠标按下后移动选中位置
lb = tkinter.Listbox(win, selectmode=tkinter.SINGLE, listvariable=lbv)
for item in ["good", "nice", "handsome", "vg", "vn"]:
    #按顺序添加
    lb.insert(tkinter.END, item)

#打印当前列表中的选项
print(lbv.get())

#设置选项
#lbv.set(("1", "2", "3"))

#绑定事件
def myPrint(event):
    print(lb.get(lb.curselection()))

#double双击button按钮1左键
lb.bind("<Double-Button-1>", myPrint)
lb.pack()

win.mainloop()