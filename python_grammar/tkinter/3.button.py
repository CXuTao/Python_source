import tkinter

def func():
    print("xt is a good man")

#创建主窗口
win = tkinter.Tk()
#设置标题
win.title("哈哈哈")
#设置大小和位置
win.geometry("400x400+200+20")


#进入消息循环

#创建按钮
button1 = tkinter.Button(win, text="按钮", command=func,
                        width=10, height=10)
button1.pack()
button2 = tkinter.Button(win, text="按钮", command=lambda :print("xt is a good man"))
button2.pack()

button3 = tkinter.Button(win, text="按钮", command=win.quit)
button3.pack()







win.mainloop()