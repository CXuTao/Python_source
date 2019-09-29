import pymysql


db = pymysql.connect("localhost", "root", "112511", "xutao")
cursor = db.cursor()


sql = "update bandcard set money=1000 where id=1"
try:
    cursor.execute(sql)
    db.commit()#写入数据库
except:
    #如果提交失败，回滚到上一次的数据
    db.rollback()

cursor.close()
db.close()