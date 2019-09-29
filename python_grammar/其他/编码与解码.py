path = r"E:\python\test2.txt"
with open(path,"wb") as f1:
    str = "hello world"
    #编码
    f1.write(str.encode("utf-8"))

with open(path,"rb") as f2:
    data = f2.read()
    print(data)
    #解码
    newData = data.decode("utf-8")
    print(newData)