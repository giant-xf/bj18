'''
创建⽣成器⽅法1
要创建⼀个⽣成器，有很多种⽅法。第⼀种⽅法很简单，只要把⼀个列表⽣
成式的 [ ] 改成 ( )'''

G =(x*2 for x in range(5))


#创建⽣成器⽅法2
    #创建生成器
def fib(times):
    n = 0
    a,b = 0,1
    while n<times:
        yield (b)  #我们在循环过程中不断调⽤ yield ，就会不断中断。
        a,b = b,a+b
        n+=1
    return 'done'
f =fib(5)


    #迭代生成器中数据，并获得返回值
while True:
    try:
        x =next(f)
        print("value:",x)
    except Exception as e:
        print("返回值为:",e)
        break

