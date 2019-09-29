import pymysql


db = pymysql.connect("192.168.222.1", "root", "112511", "xutao")
cursor = db.cursor()


sql = "delete from bandcard where money = 200"
try:
    cursor.execute(sql)
    db.commit()#写入数据库
except:
    #如果提交失败，回滚到上一次的数据
    db.rollback()

cursor.close()
db.close()