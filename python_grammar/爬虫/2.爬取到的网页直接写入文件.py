import urllib.request

urllib.request.urlretrieve("http://www.baidu.com",
                           filename=r"E:\python\爬虫\file\file2.html")

#urlretrieve在执行时会产生一些缓存
#清除缓存
urllib.request.urlcleanup()