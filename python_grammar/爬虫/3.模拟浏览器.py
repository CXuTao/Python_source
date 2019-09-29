import urllib.request
import random

url = "http://www.baidu.com"

"""
#模拟请求头
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537"
    ".36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36"
}
#设置一个请求体
req = urllib.request.Request(url,headers=headers)
#发起请求
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))
"""

agentsList = [
    "",
    "",
    "",
    ""
]

agentStr = random.choice(agentsList)
req = urllib.request.Request(url)
#向请求体里添加User_Agent
req.add_header("User-Agent", agentStr)
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))



