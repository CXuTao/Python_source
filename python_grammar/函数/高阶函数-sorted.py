#排序

#普通排序
list1 = [1,45,6,7,6,878,87,79,89]
list2 = sorted(list1)#默认升序排序
print(list1)
print(list2)


#按绝对值大小排序
list3 = [1,-45,6,-7,6,-878,87,79,89]
#key接受函数实现自定义排序规则
list4 = sorted(list3, key=abs)
print(list3)
print(list4)


#降序
list5 = [1,45,6,7,6,878,87,79,89]
list6 = sorted(list5, reverse=True)
print(list5)
print(list6)

list7 = ["b333","a2134","c22","d23456"]
list8 = sorted(list7, key=len)
print(list7)
print(list8)

def myLen(str):
    return len(str)
list9 = ["b333","a2134","c22","d23456"]
#函数可以自己写
list10 = sorted(list9, key=myLen)
print(list9)
print(list10)

