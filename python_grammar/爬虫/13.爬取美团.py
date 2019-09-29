import urllib.request
import re
import os

def image(url, toPath):
    # headers = {
    #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134"
    # }
    # req = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(url)
    HtmlStr = response.read() #要写入文件防止乱码，所以先不转换utf-8

    with open(r"E:\python\爬虫\meituan.html", "wb") as f:
       f.write(HtmlStr)
#<div class="imgbox" style="height: 125px; width: 220px;"><img src="http://p0.meituan.net/600.600/deal/ef2a03c8b11ac381e7d592b659230291348676.jpg@220w_125h_1e_1c"></div>
    # pat = r'<div class="imgbox" style="height: 125px; width: 220px;"><img src="(.*?)@>'
    # re_image = re.compile(pat, re.S)
    # imagesList = re_image.findall(HtmlStr)
    # num = 1
    # for imageURL in imagesList:
    #     path = os.path.join(toPath, str(num)+".jpg")
    #     num += 1
    #     #把图片下载到本地存储
    #     urllib.request.urlretrieve("http://"+imageURL, filename=path)
    #     print(num)

url = r"http://cq.meituan.com/meishi/b4596/"
toPath = r"E:\python\爬虫\file\file2"
image(url, toPath)
