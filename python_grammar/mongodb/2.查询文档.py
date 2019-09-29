from pymongo import MongoClient
import pymongo
from bson.objectid import ObjectId

#连接服务
conn = MongoClient("localhost", 27017)

#连接数据库
db = conn.mydb

#获取集合
collection = db.student

#查询部分文档
'''
res = collection.find({"age":{"$gt":18}})
for row in res:
    print(row)
'''

#查询所有文档
'''
res = collection.find()
for row in res:
    print(row)
'''

#统计查询
'''
res = collection.find({"age":{"$gt":18}}).count()
print(res)
'''

#根据id查询
"""
res = collection.find({"_id":ObjectId("5ca95fb9c63304263cfe6b3b")})
print(res[0])
"""

#排序
'''
#res = collection.find().sort("age")
res = collection.find().sort("age", pymongo.DESCENDING)
for row in res:
    print(row)
'''

#分页查询
res = collection.find().skip(3).limit(5)
for row in res:
    print(row)

#断开
conn.close()