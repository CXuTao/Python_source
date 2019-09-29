import tkinter

#创建主窗口
win = tkinter.Tk()
#设置标题
win.title("哈哈哈")
#设置大小和位置
win.geometry("400x400+200+20")


label1 = tkinter.Label(win, text="good", bg="blue")
label2 = tkinter.Label(win, text="nice", bg="red")
label3 = tkinter.Label(win, text="cool", bg="pink")

#绝对布局，窗口的变化对位置没有影响
label1.place(x=10, y=10)
label2.place(x=50, y=50)
label3.place(x=100, y=100)

win.mainloop()