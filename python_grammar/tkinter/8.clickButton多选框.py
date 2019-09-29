import tkinter

#创建主窗口
win = tkinter.Tk()
#设置标题
win.title("哈哈哈")
#设置大小和位置
win.geometry("400x400+200+20")


def updata():
    message = ""
    if hobby1.get() == True:
        message += "money\n"
    if hobby2.get() == True:
        message += "power\n"
    if hobby3.get() == True:
        message += "people\n"
    #清除text内容
    text.delete(0.0, tkinter.END)

    text.insert(tkinter.INSERT, message)



#进入消息循环
#要绑定的变量
hobby1 = tkinter.BooleanVar()
clickButton1 = tkinter.Checkbutton(win, text="money", variable=hobby1, command=updata)
clickButton1.pack()
hobby2 = tkinter.BooleanVar()
clickButton2 = tkinter.Checkbutton(win, text="power",  variable=hobby2, command=updata)
clickButton2.pack()
hobby3 = tkinter.BooleanVar()
clickButton3 = tkinter.Checkbutton(win, text="people",  variable=hobby3, command=updata)
clickButton3.pack()

text = tkinter.Text(win, width=50, height=5)

text.pack()





win.mainloop()