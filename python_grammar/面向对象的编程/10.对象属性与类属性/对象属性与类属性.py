class Person(object):
    #类属性，用类名来调用
    name = "hhh"
    #对象属性，对象属性的优先级高于类属性
    def __init__(self, name):
        self.name = name

    #注意：以后千万不要将对象属性与类属性重名，因为对象属性的优先级高于
    #类属性会屏蔽类属性，但是当删除对象属性后，在使用时会使用同名的类属性