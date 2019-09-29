import itertools
import time

#生成4位密码
passwd = ("".join(x) for x in itertools.product("0123456789", repeat=3))
#print(myList)
#print(len(myList))
while True:
    try:
        time.sleep(0.5)
        str = next(passwd)
    except StopIteration as e:
        break