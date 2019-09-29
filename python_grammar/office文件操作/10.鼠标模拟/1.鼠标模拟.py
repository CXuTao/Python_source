import win32con
import win32api
import time

#设置鼠标的位置
win32api.SetCursorPos([30,40])
time.sleep(0.1)

win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0)
