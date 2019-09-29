import tkinter
from tkinter import ttk

#创建主窗口
win = tkinter.Tk()
#设置标题
win.title("哈哈哈")
#设置大小和位置
win.geometry("400x400+200+20")

tree = ttk.Treeview(win)
tree.pack()

#添加一级树枝
treeF1 = tree.insert("", 0, "中国", text="中国Chi", values=("F1"))
treeF2 = tree.insert("", 1, "美国", text="美国USA", values=("F2"))
treeF3 = tree.insert("", 2, "英国", text="英国UK", values=("F3"))

#二级树枝
treeF1_1=tree.insert(treeF1, 0, "山西", text="中国山西", values=("F1_1"))
treeF1_2=tree.insert(treeF1, 1, "山东", text="中国山东", values=("F1_2"))
treeF1_3=tree.insert(treeF1, 2, "浙江", text="中国浙江", values=("F1_3"))

treeF2_1=tree.insert(treeF2, 0, "得克萨斯州", text="美国dkss", values=("F2_1"))
treeF2_1=tree.insert(treeF2, 1, "底特律", text="美国dtl", values=("F2_2"))
treeF2_1=tree.insert(treeF2, 2, "旧金山", text="美国jjs", values=("F2_3"))

#三级树枝
treeF1_1_1=tree.insert(treeF1_1, 0, "忻州", text="中国忻州", values=("F1_1_1"))
treeF1_1_2=tree.insert(treeF1_1, 1, "太原", text="中国太原", values=("F1_1_2"))

win.mainloop()