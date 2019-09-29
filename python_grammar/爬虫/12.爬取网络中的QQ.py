import urllib.request
import ssl
import re
import os
from collections import deque

def writeFileBytes(htmlBytes, toPath):
    with open(toPath, "wb") as f:
        f.write(htmlBytes)

def writeFileStr(htmlBytes, toPath):
    with open(toPath, "w") as f:
        f.write(str(htmlBytes))

def getHtmlBytse(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537"
                      ".36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36"
    }
    req = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(req)
    return response.read()

def qqCrawler(url, toPath):
    htmlBytes = getHtmlBytse(url)
    #writeFileBytes(htmlBytes,r"E:\python\爬虫\file\qqfile1.html")
    #writeFileStr(htmlBytes, r"E:\python\爬虫\file\qqfile2.txt")
    htmlStr = str(htmlBytes)


    pat = r"[1-9]\d{4,9}"
    re_qq = re.compile(pat, re.S)
    qqsList = re_qq.findall(htmlStr)
    qqsList = list(set(qqsList))  #去重
    print(qqsList)

    return qqsList


url = r"https://www.douban.com/group/topic/110094603/"
toPath = r"E:\python\爬虫\file\qqfile.txt"
#qqCrawler(url, toPath)


def center(url, toPath):
    queue = deque()
    queue.append(url)
    while len(queue) != 0:
        targetURL = queue.popleft()
        urlList = qqCrawler(targetURL, toPath)
        for item in urlList:
            tempURL = item[0]
            queue.append(tempURL)