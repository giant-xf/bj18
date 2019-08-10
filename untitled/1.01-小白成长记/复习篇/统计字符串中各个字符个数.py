s ='hello world'
a =[]
for i in s:
    if i not in a:
        print("%s :%d   "%(i,s.count(i)),end="")
    a.append(i)