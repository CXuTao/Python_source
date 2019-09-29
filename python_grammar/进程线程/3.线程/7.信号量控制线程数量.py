import threading, time

#控制线程数量
sem = threading.Semaphore(2)

def run():
    with sem:
        for i in range(10):
            print("%s--%d"%(threading.current_thread().name, i))
            time.sleep(2)

if __name__ == "__main__":
    for i in range(5):
        threading.Thread(target=run).start()