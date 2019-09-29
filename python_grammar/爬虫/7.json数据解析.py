"""

概念：一种保存数据的格式
作用：可以保存本地的json文件，更可以将json串进行传输，
      通常将json称为轻量级的传输方式

json文件组成
{}     代表对象（字典）
()     代表列表
:      代表键值对
,      分割

"""
import json

jsonStr = '{"name":"xutao", "age":18, "hobby":["money","power","english"],' \
          '"parames":{"a":1,"b":2}}'
#将json格式的字符串转换为python数据类型对象
jsonData = json.loads(jsonStr)
print(jsonData)
print(type(jsonData))
print(jsonData["hobby"])

#将python数据类型对象转换为json格式的字符串
jsonData2 = {"name":"xutao", "age":18, "hobby":["money","power","english"],' \
          '"parames":{"a":1,"b":2}}
jsonStr2 = json.dumps(jsonData2)
print(jsonStr2)

#读取本地的json文件
"""
path1 = ""
with open(path1, "rb") as f:
    data = json.load(f)
    print(data)
    print(type(data))#字典类型
"""

#写本地json
path2 = r"E:\python\爬虫\file\json1.json"
jsonData3 = {"name":"xutao", "age":18, "hobby":["money","power","english"],' \
          '"parames":{"a":1,"b":2}}
with open(path2, "w") as f:
    json.dump(jsonData3, f)
