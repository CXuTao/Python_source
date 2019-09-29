#装饰器

def func1():
    print("hello world")

def outer(func):
    def inner():
        print("*****************")
        func()
    return inner

f = outer(func1)
f()


#装饰器
def outer(func):
    def inner(age):
        if age < 0:
            age = 0
        func(age)
    return inner

#@outer表示该函数使用装饰器
@outer
def say(age):
    print("hhh is %d years old"%(age))

say(-10)
