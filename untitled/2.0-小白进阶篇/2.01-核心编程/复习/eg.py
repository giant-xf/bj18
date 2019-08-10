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
