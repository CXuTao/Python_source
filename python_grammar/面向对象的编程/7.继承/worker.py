from person import Person
class Worker(Person):
    def __init__(self, name, age):
        #调用父类的__init()__
        super(Worker, self).__init__(name, age)