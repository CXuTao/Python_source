#发邮件的库
import smtplib
#邮件文本
from email.mime.text import MIMEText

#SMTP服务器
SMTPServer = "smtp.163.com"
#发邮件的地址
sender = "xutao729919@163.com"
#发送者发送邮箱的密码
password = "XtYhN112511x"


#设置发送的内容
message = "来自爱你的徐涛的问候，哈哈哈"
#转换为邮件文本
msg = MIMEText(message)

#标题
msg["Subject"] = "涛涛"
#收件者
msg["From"] = sender

#创建SMTP服务器
mailServer = smtplib.SMTP(SMTPServer, 25)
#登录邮箱
mailServer.login(sender, password)
#发送邮件
mailServer.sendmail(sender, ["909108858@qq.com"], msg.as_string())
#退出邮箱
mailServer.quit()


