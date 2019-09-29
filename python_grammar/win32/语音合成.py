#系统客户端
import win32com.client
import time

dehua = win32com.client.Dispatch("SAPI.SPVOICE")
#dehua.Speak("hello world")

while 1:
	dehua.Speak("赵振鑫是我的好朋友")
	time.sleep(5)
