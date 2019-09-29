from pymongo import MongoClient

#连接服务
conn = MongoClient("localhost", 27017)

#连接数据库
db = conn.mydb

#获取集合
collection = db.student

collection.update({"name":"chen"}, {"$set":{"age":21}})

#断开
conn.close()
