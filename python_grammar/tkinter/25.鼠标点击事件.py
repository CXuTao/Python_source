import tkinter

#创建主窗口
win = tkinter.Tk()
#设置标题
win.title("哈哈哈")
#设置大小和位置
win.geometry("400x400+200+20")

def func(event):
    print(event.x, event.y)

#<Button-1>鼠标左键
#<Button-3>鼠标右键
#<Button-2>鼠标中间键
#<Double-Button-1>鼠标左键双击
#<Double-Button-2>鼠标中间键双击
#<Double-Button-3>鼠标右键双击
#<Triple-Button-1>鼠标左键三击
#<Triple-Button-2>鼠标中间键三击
#<Triple-Button-3>鼠标右键三击

button1 = tkinter.Button(win, text="leftmouse button")
#bind给控件绑定事件
button1.bind("<Button-1>", func)
button1.pack()

def func(event):
    print(event.x, event.y)

button2 = tkinter.Label(win, text="leftmouse button")
button2.bind("<Button-1>", func)
button2.pack()

win.mainloop()