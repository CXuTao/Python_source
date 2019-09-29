import tkinter

#创建主窗口
win = tkinter.Tk()
#设置标题
win.title("哈哈哈")
#设置大小和位置
win.geometry("400x400+200+20")

#<Enter>光标进入控件时发生
#<Leave>光标离开时触发
label = tkinter.Label(win, text="xt is a good man", bg="red")
label.pack()
def func(event):
    print(event.x, event.y)
label.bind("<Enter>", func)

win.mainloop()