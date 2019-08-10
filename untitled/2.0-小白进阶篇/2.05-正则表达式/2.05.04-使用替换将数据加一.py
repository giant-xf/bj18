import re


def add(temp):
    """将每个数据加一的函数"""
    print(temp)
    strNum = temp.group()
    result = int(strNum) + 1
    return str(result)


ret = re.sub(r"\d+",add,"py=999, c=888")
print(ret)