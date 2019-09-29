"""
self代表类的实例，而非类
self不是关键字
哪个对象调用方法那么该方法中self就代表那个对象

"""
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
        print(self.__class__)
        p = self.__class__("12", 19, 178, 56)
        print(p)
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

per = Person("xutao", 19, 178, 56)
per.say()
per.play()
per.run()