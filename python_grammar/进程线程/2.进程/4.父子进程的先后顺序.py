from multiprocessing import Process
from time import sleep
import os

def run(str):
    print("启动子进程")
    sleep(5)
    print("子进程结束")

if __name__ == "__main__":
    print("主（父）进程启动")
    p = Process(target=run, args=("nice",))
    #启动进程
    p.start()
    #父进程的结束不能影响子进程，让父进程等在子进程结束再执行父进程
    p.join()
    print("父进程结束")