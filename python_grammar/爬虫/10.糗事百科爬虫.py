import urllib.request
import re

def jokeCrawler(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537"
                      ".36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36"
    }
    req = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(req)
    HTML = response.read().decode("utf-8")
    pat = r'<div class="author clearfix">(.*?)<span class="stats-vote"><i class="number">'
    re_joke = re.compile(pat, re.S)
    divsList = re_joke.findall(HTML)
    #print(len(divsList))
    dic = {}
    for div in divsList:
        #用户名
        re_u = re.compile(r"<h2>(.*?)</h2>", re.S)
        username = re_u.findall(div)
        #print(username)
        #print(type(username))
        username = username[0]
        #print(username)
        #段子
        re_d = re.compile(r'<div class="content">\n<span>(.*?)</span>', re.S)
        duanzi = re_d.findall(div)
        duanzi = duanzi[0]
        print(duanzi)

        dic[username] = duanzi
    return dic



    #with open(r"E:\python\爬虫\file\file3.html", "w") as f:
    #    f.write(HTML)


for i in range(1,10):
    url = "https://www.qiushibaike.com/text/page/"+str(i)+"/"

info = jokeCrawler(url)