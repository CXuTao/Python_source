import pymysql


db = pymysql.connect("localhost", "root", "112511", "xutao")
cursor = db.cursor()


sql = "insert into bandcard values(0, 200), (0, 300), (0, 400), (0, 500), (0, 600)"
try:
    cursor.execute(sql)
    db.commit()#写入数据库
except:
    #如果提交失败，回滚到上一次的数据
    db.rollback()

cursor.close()
db.close()