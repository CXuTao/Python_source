import urllib.request

# 构建了两个代理Handler，一个有代理IP，一个没有代理IP
httpproxy_handler = urllib.request.ProxyHandler({"http" : "58.243.50.184"})
nullproxy_handler = urllib.request.ProxyHandler({})

proxySwitch = True #定义一个代理开关

# 通过 urllib2.build_opener()方法使用这些代理Handler对象，创建自定义opener对象
# 根据代理开关是否打开，使用不同的代理模式
if proxySwitch:
    opener = urllib.request.build_opener(httpproxy_handler)
else:
    opener = urllib.request.build_opener(nullproxy_handler)

request = urllib.request.Request("http://www.baidu.com/")

# 1. 如果这么写，只有使用opener.open()方法发送请求才使用自定义的代理，而urlopen()则不使用自定义代理。
response = opener.open(request)

# 2. 如果这么写，就是将opener应用到全局，之后所有的，不管是opener.open()还是urlopen() 发送请求，都将使用自定义代理。
# urllib2.install_opener(opener)
# response = urlopen(request)

print(response.read())