import tkinter

#创建主窗口
win = tkinter.Tk()
#设置标题
win.title("哈哈哈")
#设置大小和位置
win.geometry("400x400+200+20")


#进入消息循环

"""
输入控件
用于显示简单的文本内容

"""
#绑定变量
e = tkinter.Variable()
#show密文显示
entry = tkinter.Entry(win, show="*", textvariable=e)
entry.pack()

#e代表输入框这个对象
e.set("xt is a good man")
#取值
print(e.get())
print(entry.get())




win.mainloop()