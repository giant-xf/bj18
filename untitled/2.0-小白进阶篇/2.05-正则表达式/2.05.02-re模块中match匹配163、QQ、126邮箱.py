import re


ret1 = re.match(r"\w{4,16}@(qq|163|126)\.com$","8199@qq.com").group()
ret2 = re.match(r"\w{4,16}@(qq|163|126)\.com$","8199@163.com").group()
ret3 = re.match(r"\w{4,16}@(qq|163|126)\.com$","8199@126.com").group()



print(ret1,ret2,ret3)
