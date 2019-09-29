import tkinter
import socket
import threading

#创建主窗口
win = tkinter.Tk()
#设置标题
win.title("QQ服务器")
#设置大小和位置
win.geometry("400x400+200+20")

users = {}

def run(clientSocket, clientAddress):
    # userName = clientSocket.recv(1024)
    # users[userName] = clientSocket
    # printStr = userName + "连接"
    # text.insert(tkinter.END, printStr)
    userName = clientSocket.recv(1024)
    users[userName.decode("utf-8")] = clientSocket

    while True:
        rData = clientSocket.recv(1024)
        dataStr = rData.decode("utf-8")
        infoList = dataStr.split(":")
        users[infoList[0]].send((userName.decode("utf-8") + ":" + infoList[1]).encode("utf-8"))

def start():
    ipStr = eip.get()
    portStr = int(eport.get())
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ipStr, portStr))
    server.listen(10)
    printStr = "服务器启动成功"
    text.insert(tkinter.END, printStr)
    while True:
        clientSocket, clientAddress = server.accept()
        # print("%s --- %s 连接成功" % (str(clientSocket), clientAddress))
        t = threading.Thread(target=run, args=(clientSocket, clientAddress))
        t.start()

def startServer():
    s = threading.Thread(target=start)
    s.start()



labelIp = tkinter.Label(win,text="ip",font=("黑体", 20)).grid(row=0, column=0)

labelPort = tkinter.Label(win,text="port",font=("黑体", 20)).grid(row=1, column=0)

#绑定变量
eip = tkinter.Variable()
entryIp = tkinter.Entry(win, textvariable=eip).grid(row=0, column=1)
#绑定变量
eport = tkinter.Variable()
entryPort = tkinter.Entry(win, textvariable=eport).grid(row=1, column=1)
button = tkinter.Button(win, text="启动", command=startServer).grid(row=2, column=0)
text = tkinter.Text(win, width=30, height=4)
text.grid(row=3, column=0)
win.mainloop()