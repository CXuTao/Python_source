import tkinter
import os
from treeWindows import TreeWindows
from infoWindows import InfoWindows

win = tkinter.Tk()
win.title("目录")
win.geometry("900x400+200+50")

path = "E:\python"
infoWin = InfoWindows(win)
treeWin = TreeWindows(win, path, infoWin)





win.mainloop()