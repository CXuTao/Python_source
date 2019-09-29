import tkinter

#创建主窗口
win = tkinter.Tk()
#设置标题
win.title("哈哈哈")
#设置大小和位置
win.geometry("400x400+200+20")

#<B1-Motion>左键移动B(1,2,3) 数字表示键位(左，中，右)
label = tkinter.Label(win, text="xt is a good man")
label.pack()
def func(event):
    print(event.x, event.y)
label.bind("<B1-Motion>", func)

win.mainloop()