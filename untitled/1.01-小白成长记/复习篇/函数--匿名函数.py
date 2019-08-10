
def fun(a,b):
    sum =a+b
    return sum

print("result =",fun(1,2))


t=lambda x,y:x+y
print("result =",t(1,2))


#应用场景:
    #函数作为参数传递
    #1.自定义函数
def f(a,b,opt):
    print("result =",opt(a,b))

f(1,2,lambda x,y:x+y)


    #2.作为内置函数的参数
stus =[{"name":'老王','age':15},
       {'name':"老李",'age':16},
       {'name':"老陈",'age':17}]


stus.sort()