import socket
import threading


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("192.168.222.1", 8080))
server.listen(5)

def run(ck):
    data = clientSocket.recv(1024)
    print("客户端说：" + data.decode("utf-8"))
    #sendData = input("输入返回给客户端的数据")
    clientSocket.send("xu tao is a good man".encode("utf-8"))


while True:
    clientSocket, clientAddress = server.accept()
    #print("%s --- %s 连接成功" % (str(clientSocket), clientAddress))
    t = threading.Thread(target=run, args=(clientSocket,))
    t.start()



