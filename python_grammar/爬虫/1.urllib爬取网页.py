import urllib.request

#向指定的url地址发起请求，并返回服务器响应的数据（文件的对象）
response = urllib.request.urlopen("http://www.baidu.com")

#data = response.read().decode("utf-8")
#读取文件的全部内容，会把读取到的数据赋值给一个字符串变量
#data = response.read()
#print(data)
#print(type(data))

#读取一行
#data = response.readline()

#读取文件的全部内容，会把读取到的数据赋值给一个列表（建议使用）
data = response.readlines()
"""
print(data)
print(type(data))
print(type(data[1]))
print(len(data))
"""

#将爬取到的网页写入文件
#with open(r"E:\python\爬虫\file\file1.html", "wb") as f:
#    f.write(data)

#response 属性
#返回当前环境的一些信息
print(response.info())

#返回状态码 200表示网络请求成功 304客户端已经执行了get，但文件未发生变化
print(response.getcode())
#if response.getcode() == 200 or response.getcode == 304:
    #处理网页信息
#    pass

#返回当前正在爬取的url
print(response.geturl())

#
url = "https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=" \
      "%E5%87%AF%E5%93%A5%E5%AD%A6%E5%A0%82&oq=%25E5%2587%25AF%25E5%2593%25A5%25" \
      "E5%25AD%25A6%25E5%25A0%2582&rsv_pq=c831427900074f71&rsv_t=b1a43m%2Bi%2BV3w1W" \
      "pnTfmdfAYAvFVsf1Z0MNDsKk1kpwx9YxzaYJTKDjA3GDw&rqlang=cn&rsv_enter=0"

#解码
newUrl = urllib.request.unquote(url)
print(newUrl)
#编码
newUrl2 = urllib.request.quote(newUrl)