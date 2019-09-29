import threading

def run():
    print("xt is a good man")

#延迟执行线程
t = threading.Timer(5, run)
t.start()

t.join()
print("父线程结束")