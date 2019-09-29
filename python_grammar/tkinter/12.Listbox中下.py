import tkinter

#创建主窗口
win = tkinter.Tk()
#设置标题
win.title("哈哈哈")
#设置大小和位置
#win.geometry("400x400+200+20")


#进入消息循环
"""
列表框控件，可以包含一个或多个文本框
作用：可以在listbox控件的小窗口显示一个字符串
"""

#1.创建一个listbox,添加几个元素

#EXTENDED可以是listbox支持shift和control
lb = tkinter.Listbox(win, selectmode=tkinter.EXTENDED)
for item in ["good", "nice", "handsome", "vg", "vn", "good1",
             "nice1", "handsome1", "vg1", "vn1", "good2", "nice2", "handsome2", "vg2", "vn2"]:
    #按顺序添加
    lb.insert(tkinter.END, item)

#按住shift可以实现连选
#按住control可以实现多选

#滚动条
sc = tkinter.Scrollbar(win)
sc.pack(side=tkinter.RIGHT, fill=tkinter.Y)
lb.configure(yscrollcommand=sc.set)
lb.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
#额外给属性赋值
sc['command'] = lb.yview

lb.pack()

win.mainloop()