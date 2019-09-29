import tkinter

#创建主窗口
win = tkinter.Tk()
#设置标题
win.title("哈哈哈")
#设置大小和位置
win.geometry("400x400+200+20")


#进入消息循环

#菜单条
menubar = tkinter.Menu(win)
#菜单
menu = tkinter.Menu(menubar, tearoff=False)

#给菜单添加内容
for item in ["Python", "C", "C++", "OC", "Swift", "C#", "shell",
             "Java", "JS", "汇编", "NodeJS", "退出"]:
    menu.add_command(label=item)

menubar.add_cascade(label="语言", menu=menu)

def showMenu(event):
    menubar.post(event.x_root, event.y_root)

win.bind("<Button-3>", showMenu)
win.mainloop()