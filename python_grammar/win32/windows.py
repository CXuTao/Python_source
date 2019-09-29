import win32con
import win32gui
import time

#找出窗体的编号
QQWin = win32gui.FindWindow("TXGuiFoundation","QQ")

#隐藏窗体
#win32gui.ShowWindow(QQWin,win32con.SW_HIDE)

time.sleep(2)

#显示窗体
#win32gui.ShowWindow(QQWin,win32con.SW_SHOW)


while True:
	win32gui.ShowWindow(QQWin,win32con.SW_HIDE)
	time.sleep(0.1)
	win32gui.ShowWindow(QQWin,win32con.SW_SHOW)
	time.sleep(0.1)
