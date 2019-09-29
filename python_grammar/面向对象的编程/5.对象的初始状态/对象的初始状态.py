class Person(object):
    #定义属性
    #name = ""
    #age = 0
    #height = 0
    #weight = 0

    #定义方法
    #注意：方法的参数必须以self当第一个参数
    def run(self):
        print("run")
    def eat(self, food):
        print("eat" + food)
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

"""
构造函数：__init__()在使用类创建对象时自动调用
如果不显示的写出构造函数，默认有一个空的构造函数
"""
per = Person("xutao", 19, 178, 56)
print(per.weight)