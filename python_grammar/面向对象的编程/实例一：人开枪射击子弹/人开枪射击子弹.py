"""
人
类名：Person
属性：枪（gun）
行为：开火（fire）

枪
类名：Gun
属性：bulletBox
行为：shoot

弹夹
类名：BulletBox
属性：bulletCount

"""

from Person import Person
from BulletBox import BulletBox
from Gun import Gun

#弹夹
bulletBox = BulletBox(5)

#枪
gun = Gun(bulletBox)

#人
per = Person(gun)

per.fire()
per.fire()
per.fire()
per.fire()
per.fire()
per.fire()
per.fire()

per.fillBullet(5)
per.fire()