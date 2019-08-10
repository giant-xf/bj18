#生成器中 send用法  next()用法  __next__()用法  以及 yield 用法
'''1.next(xx)用法: 调用一次生成一个值，最后生成完了会异常
2.__next__用法:  与next用法相同
3.send()的用法: 第一次不能传入非空数据，要么不用seed()，要么传入None，
                传入temp参数，传一次更新一次，否则下次不传就默认传入了None
                可以用条件判断使其一直保持最初传入的值
                def f():
                    i=0
                    while i<5:
                        if i==0:
                            temp =yield i
                        else :
                            print(temp)
                            yield i
                        i+=1
4.yield 用法: 函数中可以参入多个yield ，变成生成器，暂停一次
'''
'''
生成器分两种 :1.生成器a =(i for i in rang(10))
              2.函数中含有yield,变成了对象，而不是函数了, 遇到yield会暂停，下一次调用继续运行
作用:协程

'''
def Num():
    i =0
    while i<5:
        temp =yield i
        print(temp)
        i +=1
t=Num()
#next(t)
#print(t.send('ooooo'))  #第一次传入数据会异常
print(t.send(None))  #第一次可以传空值
print(t.__next__())
print(t.send('hah'))
print(t.__next__())


def Num_1():
    while True:
        print('----1----')
        yield None
def Num_2():
    while True:
        print('----2----')
        yield  None
t1=Num_1()
t2=Num_2()
#while True:
    #t1.__next__()
    #t2.__next__()



