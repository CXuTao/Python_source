"""

析构函数：__del__()释放对象时自动调用

"""
class Person(object):
    def run(self):
        print("run")
    def eat(self, food):
        print("eat" + food)
    def say(self):
        print("Hello! my name is %s,I am %d years old" % (self.name, self.age))
    def play(a):
        print("play")
    def openDoor(self):
        print("我已经打开了冰箱门")
    def fillDoor(self):
        print("我已经把大象放进了冰箱")
    def closeDoor(self):
        print("我已经关上了冰箱门")
    def __init__(self, name, age, height, weight):
        #定义属性
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
    def __del__(self):
        print("这里是析构函数")

per = Person("xutao", 19, 178, 56)
