from person import Person
class Student(Person):
    def __init__(self, name, age):
        #调用父类的__init()__
        super(Student, self).__init__(name, age)
        #子类可以有独有的属性
        #子类不能访问父类的私有属性，但是能通过get set方法访问
