"""

__str__()  :print打印对象时打印该函数的返回值，给用户用的，是描述对象的方法
__repr__()  :print打印对象时自动调用，给机器用的，在Python解释器里面调用
注意：在没有str时，且有repr时，str=repr

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