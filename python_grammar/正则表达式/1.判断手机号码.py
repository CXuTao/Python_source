import re



def checkPhone(str):
    if len(str) != 11:
        return False
    elif str[0] != "1":
        return False


def checkPhone(str):
    pat = r"^1[3578]\d{9}$"
    res = re.match(pat, str)
    return res



print()