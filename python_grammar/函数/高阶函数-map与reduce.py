from functools import reduce

#map就是将数据分开处理，reduce就是将处理好的数据进行合并
#python内置了map()和reduce()函数


#map()
#原型 map(fn, lsd)
#参数一是一个函数
#参数二是一个序列

#功能：将传入的函数依次作用在序列中的每一个元素，并把结果作为新的Iterator返回

#将单个字符转为对应的字面量整数
def charToint(chr):
    return {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}[chr]

list1 = ["2", "2", "3", "5", "8", "0"]
res = map(charToint, list1)
print(res)
print(list(res))

#将整数元素的序列转为字符型
l = map(str, [1,2,3,4])
print(list(l))

#reduce(fn, lsd)
#参数一为函数
#参数二为列表
#功能：一个函数作用在序列上，这个函数必须接受两个参数，
#reduce把结果继续和序列的下一个元素累计运算


#求一个序列的和
list2 = [1,2,3,4,5]

def mySum(x, y ):
    return x + y

r = reduce(mySum, list2)
print(r)


#将字符串转为对面字面量数字
def str2int(str):
    def fc(x,y):
        return x * 10 + y
    def fs(chr):
        return {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9}[chr]
    return  reduce(fc, map(fs, list(str)))

a = str2int("12345")
print(a)


def myMap(func, li):
    resList = []
    for parase in li:
        res = func(parase)
        resList.append(res)
    return resList

