import pymysql


db = pymysql.connect("localhost", "root", "112511", "xutao")
cursor = db.cursor()

#检查表是否存在，存在则删除
cursor.execute("drop table if exists bandcard")

sql = "create table bandcard(id int auto_increment primary key, money int not null)"
cursor.execute(sql)

cursor.close()
db.close()
