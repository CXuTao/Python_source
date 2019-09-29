import tkinter
#创建主窗口
win = tkinter.Tk()
#设置标题
win.title("哈哈哈")
#设置大小和位置
win.geometry("400x400+200+20")


#进入消息循环
"""
Label：标签控件显示文本
"""
#win:父窗体
#text：显示文本
#bg:背景色
#fg:字体颜色
#wraplength:制定text文本中多宽进行换行
#justify:设置换行后的对其方式
#anchor：文字的位置 s南 w西 e东 n北 center居中 en 等等
label = tkinter.Label(win,
                      text="xt",
                      bg="pink",
                      fg="red",
                      font=("黑体", 20),
                      width=10,
                      height=4,
                      wraplength=100,
                      justify="left",
                      anchor="e")
#显示出来
label.pack()







win.mainloop()