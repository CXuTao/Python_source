"""

TCP是建立可靠连接，并且通信双方都可以以流的形式发送数据，相对于TCP，
UDP则是面向无连接的协议

使用UDP协议时，不需要建立连接，只需要知道对方的IP地址和端口号，
就可以直接发送数据包，但是能不能到达就不知道了

虽然UDP传输数据不可靠，但他的优点是，和TCP比，速度快，对于要求不
高的数据可以使用UDP

"""

import socket
import time

str = "1_1bt4_10#32499#002481627512#0#0#0:1289671407:a:b:288:发送文本"
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp.connect(("IP地址", 2425))
while True:
    udp.send(str.encode("gbk"))
    time.sleep(1)


