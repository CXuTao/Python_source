class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print("run")

    def eat(self, food):
        print("eat " + food)