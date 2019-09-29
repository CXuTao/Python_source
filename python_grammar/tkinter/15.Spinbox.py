import tkinter

#创建主窗口
win = tkinter.Tk()
#设置标题
win.title("哈哈哈")
#设置大小和位置
win.geometry("400x400+200+20")


#进入消息循环
"""
数值范围控件
"""

def updata():
    print(v.get())

#绑定变量
v = tkinter.StringVar()
#increment步长默认为1
#values:值只能取元组中的，最好不要与from_ to 同时使用values=(0,2,4,6,8)),
#command只要值改变就执行相应方法
sp = tkinter.Spinbox(win, from_=0, to=100, increment=1, textvariable=v, command=updata)
sp.pack()

#赋值
v.set(20)
#取值
print(v.get())

win.mainloop()