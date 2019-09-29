
class Person(object):
    def __init__(self, age):
        #属性直接对外暴露
        #self.age = age
        #使用限制访问
        self.__age = age

    """

    def getAge(self):
        return self.__age
    def setAge(self, age):
        if age < 0:
            age = 0
        self.__age = age
    """
    #就是相当于get,set方法
    #方法名为受限的变量去掉下划线
    @property
    def age(self):
        return self.__age
    @age.setter    #去掉下划线.setter
    def age(self, age):
        if age < 0:
            age = 0
        self.__age = age


per = Person(19)

#属性直接对外暴露
#不安全没有数据过滤
#per.age = -10
print(per.age)

#使用限制访问
#print(per.getAge())
#per.setAge(20)
#print(per.getAge())

#property可以让你对受限的属性使用电语法

