import tkinter

#创建主窗口
win = tkinter.Tk()
#设置标题
win.title("哈哈哈")
#设置大小和位置
win.geometry("400x400+200+20")


#进入消息循环
"""
列表框控件，可以包含一个或多个文本框
作用：可以在listbox控件的小窗口显示一个字符串
"""

#1.创建一个listbox,添加几个元素
lb = tkinter.Listbox(win, selectmode=tkinter.BROWSE)
for item in ["good", "nice", "handsome", "vg", "vn"]:
    #按顺序添加
    lb.insert(tkinter.END, item)
#在开始添加
lb.insert(tkinter.ACTIVE, "cool")
#将列表当成一个元素添加
#lb.insert(tkinter.END, ["very good", "very nice"])
#删除
#参数1为开始的索引，参数二为结束的索引，如果不指定参数二，
# 只删除第一个索引引出的内容
#lb.delete(1, 3)
#lb.delete(1)
#选中
#参数1为开始的索引，参数二为结束的索引，如果不指定参数二，
# 只选中第一个索引引出的内容
lb.select_set(2, 4)
#lb.select_set(1)
#取消选择
#参数1为开始的索引，参数二为结束的索引，如果不指定参数二，
# 只取消第一个索引引出的内容
lb.select_clear(2, 5)
lb.select_clear(3)

#获取列表中元素个数
print(lb.size())

#从列表中取值
print(lb.get(2, 4))
print(lb.get(3))

#返回当前的索引项,不是item元素
print(lb.curselection())
lb.pack()

#判断一个选项是否被选中
print(lb.select_includes(1))


win.mainloop()