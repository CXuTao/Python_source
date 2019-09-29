from child import Child
def main():
    c = Child(300, 100)
    print(c.money, c.faceValue)
    c.play()
    c.eat()
    #父类中方法名相同，默认调用在括号中排前面的父类的方法
    c.func()




if __name__ == "__main__":
    main()