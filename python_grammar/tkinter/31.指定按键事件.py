import tkinter

#创建主窗口
win = tkinter.Tk()
#设置标题
win.title("哈哈哈")
#设置大小和位置
win.geometry("400x400+200+20")


#匹配特定按键
label = tkinter.Label(win, text="xt is a good man", bg="red")
label.pack()
label.focus_set()
def func(event):
    print("event.chr = ", event.char)
    print("event.keycode = ", event.keycode)
label.bind("a", func)

win.mainloop()