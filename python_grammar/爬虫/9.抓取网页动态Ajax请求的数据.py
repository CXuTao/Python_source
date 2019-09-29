import urllib.request
import ssl
import json


def ajaxCrawler(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537"
                      ".36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36"
    }
    req = urllib.request.Request(url, headers=headers)

    #使用ssl创建未验证的上下文(在高版本Python中不加也不会报错)
    context = ssl._create_unverified_context()
    response = urllib.request.urlopen(req, context=context)

    jsonStr = response.read().decode("utf-8")
    jsonData = json.loads(jsonStr)

    return jsonData

url = "https://movie.douban.com/j/chart/top_list?type=17&interval_id=100%3A90&action=&start=20&limit=20"
info = ajaxCrawler(url)
print(info)

for i in range(1,10):
    url = "https://movie.douban.com/j/chart/top_list?type=17&interval_" \
          "id=100%3A90&action=&start="+str(i * 20)+"&limit=20"
    info = ajaxCrawler(url)
    print(info)
    print(len(info))
