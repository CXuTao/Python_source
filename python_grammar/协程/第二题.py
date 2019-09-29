def operator():
    #定义一个列表存放输入的分数
    nums = []
    flag = True
    while flag:
        numm = input("请输入分母：")
        numc = input("请输入分子：")
        tnum = int(numc) / int(numm)
        nums.append(tnum)

        tflag = input("是否输入下一个分数，yes/no")
        if tflag == "no":
            flag = False
    #print(nums)

def main():
    operator()


if __name__ == "__main__":
    main()








