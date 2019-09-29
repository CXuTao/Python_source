from XTmysql import XTmysql

s = XTmysql("localhost", "root", "112511", "xutao")


res = s.get_all("select * from bandcard where money>400")
for row in res:
    print("%d--%d" % (row[0], row[1]))