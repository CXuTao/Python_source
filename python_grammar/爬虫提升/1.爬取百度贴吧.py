import urllib.request
import urllib.parse


def loadPage(url, fileName):
    '''
            作用：根据url发送请求，获取服务器响应文件
            url：需要爬取的url地址
            filename: 文件名
     '''
    print("正在下载" + fileName)
    header = {
         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537"
                      ".36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36"
    }
    req = urllib.request.Request(url, headers=header)
    response = urllib.request.urlopen(req)
    return response.read()


def writeFile(html, fileName):
    """
           作用：保存服务器响应文件到本地磁盘文件里
           html: 服务器响应文件
           filename: 本地磁盘文件名
    """
    print("正在存储" + fileName)
    with open(fileName, "w") as f:
        f.write(str(html))
    print("-" * 20)

def tiebaSpider(url, beginPage, endPage):
    """
           作用：负责处理url，分配每个url去发送请求
           url：需要处理的第一个url
           beginPage: 爬虫执行的起始页面
           endPage: 爬虫执行的截止页面
       """

    for page in range(beginPage, endPage + 1):
        pn = (page - 1) * 50

        fileName = "第" + str(page) + "页.html"
        # 组合为完整的 url，并且pn值每次增加50
        fullURL = url + "&pn=" + str(pn)

        # 调用loadPage()发送请求获取HTML页面
        html = loadPage(fullURL, fileName)
        # 将获取到的HTML页面写入本地磁盘文件
        writeFile(html, fileName)














if __name__ == "__main__":

    kw = input("请输入要爬取的贴吧：")
    #输入起始页和终止页
    beginPage = int(input("请输入起始页："))
    endPage = int(input("请输入终止页："))

    url = "http://tieba.baidu.com/f?"
    key = urllib.parse.urlencode({"kw" : kw})

    # 组合后的url示例：http://tieba.baidu.com/f?kw=lol
    url = url + key
    tiebaSpider(url, beginPage, endPage)