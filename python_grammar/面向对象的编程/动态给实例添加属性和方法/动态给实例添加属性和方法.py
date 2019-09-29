from types import MethodType
#创建一个空类
class Person(object):
    #要添加属性，只能添加在元组中有的
    __slots__ = ("name", "age", "speak")



per = Person()
#动态添加属性，这体现了动态语言灵活的特点
per.name = "xy"
print(per.name)
#动态添加方法
"""
def say(self):
    print("my name is " + self.name)
per.speak = say
per.speak()
"""
def say(self):
    print("my name is " + self.name)
per.speak = MethodType(say, per)
per.speak()

#我们想要限制实例的属性
#比如，只允许给对象添加name,age,height,weight属性

#解决：定义类时，定义一个特殊的属性（__slots__）,可以限制动态添加的属性