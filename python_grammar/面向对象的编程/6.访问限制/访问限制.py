class Person(object):
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
    def __init__(self, name, age, height, weight, money):
        #定义属性
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.__money = money
    def setMoney(self, money):
        if money < 0:
            money = 0
        self.__money = money
    def getMoney(self):
        return self.__money

#Python没有绝对的私有

#让内部的属性不让外部直接修改,在属性前加两个下划线,在Python中，如果在属性前加两下划线
#属性就变成了私有属性，不能外部访问，只能内部访问
#在Python中 __XX__ 叫做特殊变量，不是私有变量，一般是系统写好的，一般不这样定义
#不能直接访问per.__money是因为Python解释器把__money变成_Python__money
#仍可以用_Person__money去访问，但是强烈要求不要这么干，不同解释器解释的变量名可能不一样
#在Python中 _XX_这样的实例变量外部也是可以访问的，按照约定的规则，当我们看到这样的变量时
#要当成私有的，在外部不要访问