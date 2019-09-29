from pymongo import MongoClient

#连接服务
conn = MongoClient("localhost", 27017)

#连接数据库
db = conn.mydb

#获取集合
collection = db.student

#添加文档
collection.insert([{"name":"chen", "age":19, "gender":1, "address":"福建", "isDelete":0},
                   {"name":"chen2", "age":19, "gender":1, "address":"福建", "isDelete":0}])

#断开
conn.close()











