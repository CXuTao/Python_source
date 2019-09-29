class Person(object):
    #定义属性
    name = ""
    age = 0
    height = 0
    weight = 0

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

per1 = Person()
print(per1)

per2 = Person()
print(per2)

"""
访问属性
格式：对象名.属性名 
赋值：对象名.属性名 = 新值
"""
per = Person()
per.name = "xutao"
per.age = 19
per.height = 178
per.weight = 56
print(per.name)
per.openDoor()
per.fillDoor()
per.closeDoor()
per.eat("苹果")