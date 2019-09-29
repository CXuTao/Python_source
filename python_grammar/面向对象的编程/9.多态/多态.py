from cat import Cat
from mouse import Mouse
from person import Person

"""
多态：一种事物的多种形态

最终目标：人可以喂任何一种动物

"""

tom = Cat("tom")
jerry = Mouse("jerry")

tom.eat()
jerry.eat()



#定义一个人类，可以喂猫和老鼠
per = Person()
#per.feedCat(tom)
#per.feedMouse(jerry)

#人要喂一百种动物
per.feedAnimal(tom)
per.feedAnimal(jerry)