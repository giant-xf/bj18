import re


a ="4"
b ="55"
c ="100"


ret1 = re.match("[1-9]?[1-9]",a)
ret2 = re.match("[1-9]?[1-9]",b)
ret3 = re.match("[1-9]?[1-9]",c)
ret4 = re.match("[1-9]?[1-9]","02")
print(ret1,ret2,ret3,ret4)



#匹配0-100的数字
#方法一
re.match(r"[1-9]?\d?$|100$","100")
#方法二
re.match(r"[1-9]\d?$|0$|100$","0")


