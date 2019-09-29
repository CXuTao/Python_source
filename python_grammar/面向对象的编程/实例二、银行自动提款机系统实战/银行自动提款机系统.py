"""
人
类名：Person
属性：姓名 身份证号 电话号 卡
行为：


卡
类名：Card
属性：卡号 密码 余额
行为：

银行
类名：Bank
属性：用户列表 提款机


提款机
类名： ATM
属性：用户字典
行为：开户 查询 取款 存款 转账 改密 锁定 解锁 补卡 销户


管理员
类名：Ad1min
属性：
行为：管理员界面 管理员登录 管理员验证 系统功能界面
"""
from admin import Admin
from atm import ATM
import time
import pickle
import os

def main():
    # 管理员对象
    admin = Admin()
    # 管理员开机
    admin.printAdminView()
    if admin.adminOption():
        return -1

    #存储所有用户的信息
    #allUsers = {}

    #提款机对象
    filePath = os.path.join(os.getcwd(), "allusers.txt")
    f = open(filePath, "rb")
    allUsers = pickle.load(f)
    atm = ATM(allUsers)


    while True:
        admin.printSysFunctionView()
        #等待用户操作
        option = input("请输入您的操作：")
        if option == "1":
            #开户
            atm.creatUser()
        elif option == "2":
            # 查询
            atm.searchUserInfo()
        elif option == "3":
            # 取款
            atm.get1Money()
        elif option == "4":
            # 存款
            print("存款")
        elif option == "5":
            #转账
            print("转账")
        elif option == "6":
            # 改密
            print("改密")
        elif option == "7":
            # 锁定
            atm.lockUser()
        elif option == "8":
            # 解锁
            atm.unlockUser()
        elif option == "9":
            # 补卡
            print("补卡")
        elif option == "0":
            #销户
            print("销户")
        elif option == "a":
            #退出
            if not admin.adminOption():
                #将当前用户信息保存到文件中去
                f = open(filePath, "wb")
                pickle.dump(atm.allUsers, f)
                f.close()
                return -1

        time.sleep(2)



if __name__ == "__main__":
    main()