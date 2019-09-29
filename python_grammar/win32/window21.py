import win32con
import win32gui
import time
import random

#找出窗体的编号
QQWin = win32gui.FindWindow("TXGuiFoundation","QQ")

#参数一：控制的窗体
#参数二：大致方向，HWND_TOPMOST上方
#参数三：位置x
#参数四：位置y
#参数五：长度
#参数六：宽度

#win32gui.SetWindowPos(QQWin,win32con.HWND_TOPMOST,100,100,50,50,win32con.SWP_SHOWWINDOW)

while True:
	x = random.randrange(1000)
	y = random.randrange(500)
	win32gui.SetWindowPos(QQWin,win32con.HWND_TOPMOST,x,y,300,300,win32con.SWP_SHOWWINDOW)
	time.sleep(0.1)
