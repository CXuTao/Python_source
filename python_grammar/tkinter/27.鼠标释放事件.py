import tkinter

#创建主窗口
win = tkinter.Tk()
#设置标题
win.title("哈哈哈")
#设置大小和位置
win.geometry("400x400+200+20")


#<ButtonRelease-1>释放鼠标左键
#<ButtonRelease-2>释放鼠标中间键
#<ButtonRelease-3>释放鼠标右键
label = tkinter.Label(win, text="xt is a good man", bg="red")
label.pack()
def func(event):
    print(event.x, event.y)
label.bind("<ButtonRelease-1>", func)

win.mainloop()