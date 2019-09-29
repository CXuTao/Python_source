import itertools

#生成4位密码
myList = list(itertools.product([1,2,3,4],repeat=4))
print(myList)
print(len(myList))
