from time import sleep

def run():
    while True:
        print("xutao is a nice man")
        sleep(1)

if __name__ == "__main__":
    while True:
        print("xutao is a good man")
        sleep(1)
    #不会执行，只有循环结束才可以
    run()