import telnetlib

def telnetDoSomething(IP, user, password, command):

    try:
        # 连接服务器
        telent = telnetlib.Telnet(IP)
        # 设置调试级别
        telent.set_debuglevel(2)

        # 读取信息
        rt = telent.read_until("Login username:".encode("utf-8"))
        # 写入用户名
        telent.write((user + "\r\n").encode("utf-8"))

        # 输入密码
        rt = telent.read_until("Login password:".encode("utf-8"))
        # 写入密码
        telent.write((password + "\r\n").encode("utf-8"))

        # 验证IP
        rt = telent.read_until("Domain name:".encode("utf-8"))
        # 写入IP
        telent.write((IP + "\r\n").encode("utf-8"))

        # 登陆成功
        rt = telent.read_until(">".encode("utf-8"))
        # 写命令
        telent.write((command + "\r\n").encode("utf-8"))

        # 上面命令执行成功会继续读到>
        rt = telent.read_until(">".encode("utf-8"))

        # 断开连接
        telent.close()
        return True
    except:
        return False


if __name__ == "__main__":
    IP = ""
    user = ""
    password = ""
    command = ""
    telnetDoSomething(IP, user, password, command)