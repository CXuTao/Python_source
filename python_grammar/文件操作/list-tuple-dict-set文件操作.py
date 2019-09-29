import pickle
myList = (1,2,3,4,5,"hello world")
path = r"E:\python\test2.txt"
f = open(path,"wb")

pickle.dump(myList,f)
f.close()

#读取
f1 = open(path,"rb")
tempList = pickle.load(f1)
print(tempList)
f1.close()