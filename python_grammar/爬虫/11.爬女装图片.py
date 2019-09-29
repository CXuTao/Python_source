import urllib.request
import re
import os

def image(url, toPath):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537"
                      ".36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36"
    }
    req = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(req)
    HtmlStr = response.read().decode("utf-8")  #要写入文件防止乱码，所以先不转换utf-8

    #with open(r"E:\python\爬虫\yhd.html", "wb") as f:
    #    f.write(HtmlStr)

    pat = r'<img width="220" height="282" class="err-product" data-img="1" source-data-lazy-img="//(.*?)" />'
    re_image = re.compile(pat, re.S)
    imagesList = re_image.findall(HtmlStr)
    num = 1
    for imageURL in imagesList:
        path = os.path.join(toPath, str(num)+".jpg")
        num += 1
        #把图片下载到本地存储
        #urllib.request.urlretrieve("http://"+imageURL, filename=path)
        urllib.request.urlretrieve("http://" + imageURL, filename=path)
        print(num)

url = r"https://search.jd.com/Search?keyword=%E" \
      r"8%BF%9E%E8%A1%A3%E8%A3%99%E8%95%BE%E4%B8%9D" \
      r"&enc=utf-8&wq=%E8%BF%9E%E8%A1%A3%E8%A3%99%E8%95" \
      r"%BE%E4%B8%9D&pvid=293a666b56e34cdc9fa97f2325f294bb"
toPath = r"E:\python\爬虫\file\image"
image(url, toPath)
