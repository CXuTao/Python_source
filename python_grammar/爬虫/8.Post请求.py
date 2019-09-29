"""

特点：把参数进行打包，单独传输

优点：数量大、安全（当对服务器数据进行修改时建议使用post请求）

缺点：速度慢

"""
import urllib.request
import urllib.parse  #对参数进行打包

url = "http://www.sunck.wang:8085/form"
#将要发送的数据合成一个字典
#字典的键去网址里找，一般为input标签的name属性的值
data = {
    "username":"sunck",
    "passwd":"666"
}
#对要发送的数据进行打包，记住编码
postData = urllib.parse.urlencode(data).encode("utf-8")
#请求体
req = urllib.request.Request(url, data=postData)
#请求
#opener = urllib.request.build_opener()
req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537"
    ".36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36")
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))