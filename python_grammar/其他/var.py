number1 = input("请输入一个数字：")

number2  = input("请继续输入一个数：")

print("number1 + number2 = ",number1 + number2)

number3 = int(input("请输入一个数字："))

number4 = int(input("请继续输入一个数："))

print("number3 + number4 = ",number3 + number4)

#查看变量的类型
print(type(number1))
#查看变量的地址
print(id(number1))
#删除变量以后不能访问
del number1