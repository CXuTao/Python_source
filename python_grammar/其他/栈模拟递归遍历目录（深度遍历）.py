import os

def getAllDirDE(path):
    stack = []
    stack.append(path)

    #处理栈,栈空时结束循环
    while len(stack) != 0:
        #从栈里取出数据
        dirPath = stack.pop()
        filesList = os.listdir(dirPath)

        #处理每一个文件，普通文件打印出来，目录压栈
        for fileName in filesList:
            fileAbsPath = os.path.join(dirPath,fileName)
            if os.path.isdir(fileAbsPath):
                #是目录则压栈
                print("目录：" + fileName)
                stack.append(fileAbsPath)
            else:
                #打印普通文件
                print("普通：" + fileName)




getAllDirDE("E:\\")