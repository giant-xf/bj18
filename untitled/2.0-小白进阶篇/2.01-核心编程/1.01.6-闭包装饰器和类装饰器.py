'''
test 和 test()区别   函数和变量一样，都是引用，test表示函数名，可以使用a=test ，这样
a()和test()效果一样，

'''
#装饰器原理
'''
def w1(func):
    #print('正在装饰')
    def inner():
        print('----验证1-----')
        func()
    return inner

def f1():
    print('---f1----')

def f2():
    print('---f2----')

f1=w1(f1)
f2=w1(f2)
f1()
f2()
'''
# 多个装饰器装饰的函数
#装饰器 就是 闭包
def w1(func):
    print('正在装饰1')
    def inner():
        print('----验证1-----')
        func()
    return inner
def w2(func):
    print('正在装饰2')
    def inner():
        print('----验证2-----')
        func()
    return inner
@w1 #f1=w1(f1)
@w2 #f1=w2(f1)
def f1():
    print('---f1----')
# @w1
# def f2():
#     print('---f2----')
f1()
#小结: 装饰器是装饰的函数 ，且程序运行到装饰器就开始装饰，并非调用函数后才开始装饰
#      装饰器由下到上装饰，而调用是从上到下

print('-'*30)

#带参数的和返回值得装饰器
#带参数和返回值通用的装饰器
'''
def w1(func):
    print('正在装饰1')
    def inner(*args,**kwargs):
        print('----验证1-----')
        ret =func(*args,**kwargs)   #接受返回的值
        return  ret     #返回被装饰函数的返回值
    return inner
'''
#带返回值
def w1(func):
    print('正在装饰1')
    def inner(*args,**kwargs):
        print('----验证1-----')
        ret =func(*args,**kwargs)
        return  ret
    return inner
@w1 #f1 =w1(f1)
def f1(): #然后f1指向了inner，func 指向了f1，
    print('---f1----')
    return '我是带返回值的函数'
ret =f1()
print('%s'%ret)
#带参数
@w1
def f2(a,b):
    print('---f2--a=%d,b=%d--'%(a,b))

ret =f2(11,22)
print('返回值为%s'%ret)

print('-'*30)


#带参数的装饰器
def func_arg(arg ='hello'):
    def w1(func):
        print('正在装饰')
        def inner():
            print('-----验证1--%s---'%arg)
            func()
        return inner
    return w1

@func_arg('heiheiehi')
def f1():
    print('------f1-----')

f1()
#想要传入参数，必须在外面再套一层函数，

print('-'*30)

#类装饰器
class Test(object):
    def __init__(self,func):
        print('----初始化----')
        print('func  name is %s'%func.__name__)
        self.__func =func

    def __call__(self, *args, **kwargs):
        print('装饰器中的功能')
        self.__func()
@Test
def fun():
    print('-----fun fun fun----')

#t1 =Test(fun)
fun()
