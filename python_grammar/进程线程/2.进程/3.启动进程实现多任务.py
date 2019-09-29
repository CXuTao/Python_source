"""

multiprocessing 库
跨平台版本的多进程模块，提供了Process类来代表一个进程对象

"""
from multiprocessing import Process
from time import sleep
import os

def run(str):
    while True:
        #getpid()获得当前进程id号
        #getppid()获取当前进程的父进程
        print("xutao is a {} man   ------{}--{}".format(str, os.getpid(), os.getppid()))
        sleep(2)

if __name__ == "__main__":
    print("主（父）进程启动---%s"%os.getpid())
    #创建子进程
    #target说明进程执行的任务
    #元组如果只有一个元素后面一定要有一个逗号
    p = Process(target=run, args=("nice",))
    #启动进程
    p.start()
    while True:
        print("xutao is a good man")
        sleep(1)