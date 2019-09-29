#引入模块
#import语句
#格式：import module1...

#引入了自定义模块，不用加.py后缀，报错忽略掉
import xutao
#注意：一个模块只会被引入一次，不管引入多少次，防止模块多次引入

#使用模块中的内容
#格式：模块名.函数名/变量名
xutao.sayGood()
print(xutao.tt)