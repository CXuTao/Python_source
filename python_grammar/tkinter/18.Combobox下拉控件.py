import tkinter
from tkinter import ttk

#创建主窗口
win = tkinter.Tk()
#设置标题
win.title("哈哈哈")
#设置大小和位置
win.geometry("400x400+200+20")


#进入消息循环
cv = tkinter.StringVar()
com = ttk.Combobox(win, textvariable=cv)
com.pack()
#设置下拉数据
com["value"] = ("黑龙江", "吉林", "辽宁")
#设置默认值
com.current(0)

def func(event):
    print(com.get())
    print(cv.get())
    print("hello world")
#绑定事件
com.bind("<<ComboboxSelected>>", func)

win.mainloop()