import tkinter

#创建主窗口
win = tkinter.Tk()
#设置标题
win.title("哈哈哈")
#设置大小和位置
win.geometry("400x400+200+20")

#<Key>相应所有的按键
label = tkinter.Label(win, text="xt is a good man", bg="red")
label.pack()
#设置焦点
#小控件的时候有焦点才能相应键盘事件，键盘事件其实是作用在焦点身上，但是win上的事件不需要
label.focus_set()
def func(event):
    print("event.chr = ", event.char)
    print("event.keycode = ", event.keycode)
label.bind("<Key>", func)

win.mainloop()