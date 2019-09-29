import tkinter

#创建主窗口
win = tkinter.Tk()
#设置标题
win.title("哈哈哈")
#设置大小和位置
#win.geometry("400x400+200+20")


#进入消息循环

"""
文本控件，显示多行文本
"""
#创建滚动条
scroll = tkinter.Scrollbar()
text = tkinter.Text(win, width=30, height=4)
#side放到窗体的哪一侧 fill填充
scroll.pack(side=tkinter.RIGHT, fill=tkinter.Y)
text.pack(side=tkinter.LEFT, fill=tkinter.Y)

#关联
#滚动条动控制文本动
scroll.config(command=text.yview)
#文本动控制滚动条动
text.config(yscrollcommand=scroll.set)
str = "六月是离别的季节。和朝夕相处了四年的同学一一告别后，"+\
      "我收拾好行李，正式地从一个狗窝搬进了另一个狗窝。虽然房子是租的，但是生活是自己的。」"+\
      "坚持这一理念的我，还是花了不少心思在装扮房间上。经过了一天的收拾，我看了看房间的每一个角落"+"" \
      "，确保都是我满意的样子后，我心满意足地躺在了床上。但当我认为所有事情都准备妥当了，新生活已经在向我招手时"+\
"，现实又一次狠狠地甩了我一个耳光。「嗡~」，差点忘了，六月也是驱蚊的季节。"
text.insert(tkinter.INSERT, str)







win.mainloop()