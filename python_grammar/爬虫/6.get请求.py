"""

特点：把数据拼接到请求路径的后面传递给服务器
优点：速度快
缺点：承载能力小，不安全

"""
import urllib.request
url = "http://www.sunck.wang:8085/sunck"
response = urllib.request.urlopen()
#获取返回数据
data = response.read().decade("utf-8")
print(data)