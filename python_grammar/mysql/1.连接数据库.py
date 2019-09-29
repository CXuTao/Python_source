import pymysql

#连接数据库
#参数一：mysql服务所在主机的IP
#参数二：用户名
#参数三：密码
#参数四：要连接的数据库名
db = pymysql.connect("192.168.222.1", "root", "112511", "xutao")

#创建一个cursor对象
cursor = db.cursor()

sql = "select version()"

#执行sql语句
cursor.execute(sql)

#获取返回信息
data = cursor.fetchall()
print(data)
#断开连接
cursor.close()
db.close()




