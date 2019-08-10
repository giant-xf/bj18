import re

s = ["http://www.interoem.com/messageinfo.asp?id=35",
"http://3995503.com/class/class09/news_show.asp?id=14"]

x = "http://www.interoem.com/messageinfo.asp?id=35"

for i in s:
    r = re.sub(r"(http.+?com/).*",lambda x:x.group(1),i)
    print(r)


a = 'hello world ha ha'

#方法一(切掉分隔符)
r1 = re.split(r" ",a)
#方法二(提取字符)
r2 =re.findall(r"\b[a-zA-Z]+\b",a)

print(r1)
print(r2)
