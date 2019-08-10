def f1(fn):
    def w():
        #return '<b>'+fn()+'</b>'
        print('sssssssss')
        return fn()    #若被装饰函数有返回值，这里必须接收然后再打印，否则为 None
    return w

def f2(fn):
    def w():
        #return '<i>'+fn()+'</i>'
        fn()
    return w

@f1
def test1():
    return ('----text1')

@f2
def test2():
    return ('----text2')

#先运行@f1再运行@f2
@f2
@f1
def test3():
    return ('-----text3')

print(test1())
print(test2())
print(test3())



#装饰器的用途，主功能不需要修改，修改外部就行
from time import *
def timefun(func):
    def wrappedfunc(*args,**kwargs):
        print("%s called at %s"%(func.__name__, ctime()))

        return func(*args,**kwargs)  #加上return更加通用，避免出现返回值为None

    return wrappedfunc
@timefun
def foo(a,b,c):
    print(a+b+c)
    #return (a+b+c)
foo(1,2,3)

#装饰器带参数
from time import *
def fu(pre='hello'):
    def timefun(func):
        def wrappedfunc(*args,**kwargs):
            print("%s called at %s %s"%(func.__name__, ctime(),pre ))

            func(*args,**kwargs)

        return wrappedfunc

    return timefun
@fu('python')
def foo():
    print('I am foo')

foo()


#类装饰器(非重点)
'''
装饰器函数其实是这样⼀个接⼝约束，它必须接受⼀个callable对象作为参
数，然后返回⼀个callable对象。在Python中⼀般callable对象都是函数，但
也有例外。只要某个对象重写了 __call__() ⽅法，那么这个对象就是
callable的。

'''

class Test(object):

    def __init__(self,func):
        print('-----初始化----')
        print('函数的名字是:',func.__name__)
        self.__func =func

    def __call__(self, *args, **kwargs):
        print('-----装饰器中的功能----')
        return  self.__func()

@Test
def test():
    print("----test----")

t =test()

#说明：
#1. 当⽤Test来装作装饰器对test函数进⾏装饰的时候，⾸先会创建Test的实例对象
# 并且会把test这个函数名当做参数传递到__init__⽅法中
# 即在__init__⽅法中的func变量指向了test函数体
#
#2. test函数相当于指向了⽤Test创建出来的实例对象
#
#3. 当在使⽤test()进⾏调⽤时，就相当于让这个对象()，因此会调⽤这个对象的__call__⽅法
#
#4. 为了能够在__call__⽅法中调⽤原来test指向的函数体，所以在__init__⽅法中就需要⼀个实例属性来保存这个函数体的引⽤
# 所以才有了self.__func = func这句代码，从⽽在调⽤__call__⽅法中能够调⽤到test之前的函数体


