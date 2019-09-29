import tkinter

#创建主窗口
win = tkinter.Tk()
#设置标题
win.title("哈哈哈")
#设置大小和位置
win.geometry("400x400+200+20")


#进入消息循环

def updata():
    print(r.get())


#一组单选框绑定同一变量
r = tkinter.IntVar()
radio1 = tkinter.Radiobutton(win, text="one", value="1", variable=r, command=updata)
radio1.pack()

radio2 = tkinter.Radiobutton(win, text="two", value="2", variable=r, command=updata)
radio2.pack()





win.mainloop()