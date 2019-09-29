"""
设计类
类名：见名知意，首字母大写，其它遵循驼峰原则
属性：见名知意，其它遵循驼峰原则
行为（方法功/能）：见名知意，其它遵循驼峰原则
"""

"""
创建类
类：一种数据类型，本身并不占内存空间，
实例化的对象占据内存空间

格式：
class 类名（父类列表）：
    属性
    行为
"""
#object：基类，超类，所有类的父类
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



