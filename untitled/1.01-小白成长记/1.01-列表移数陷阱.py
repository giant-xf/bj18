a =[11,22,33,44,55,66]
b =[]
'''
列表如果33被删除，那么44会迅速补上33的位置
那个44就不会被删除  
出现漏删

一次循环删不掉
若无限次循环，则会删掉
'''
def fun():
    for i in a:
        if  i ==33 or i ==44:
            a.remove(i)
    print(a)
def fun1():
    for i in a:
        if i ==3 or i==44:
            b.append(i)

    for i in b:
        a.remove(i)

    print(a)

fun()
print('---------')
fun1()