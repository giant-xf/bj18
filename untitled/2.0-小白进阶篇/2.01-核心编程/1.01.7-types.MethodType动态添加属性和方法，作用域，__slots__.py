#globals() 和 locals()
#globals: 可以显示当前作用域的所有的全局变量
#locals :可以显示当前作用域的所有的局部变量
'''
num =100
def f1():
    num =200
    def f2():
        num =300
        print(locals())
        print(globals())
    return f2

a1 =f1()
a1()
'''
#体现了python中动态修改属性
'''
class Num(object):
    age =10
    def __init__(self,newname):
        self.name =newname
t =Num('laowang')
print(t.age)
print(t.name)
#del t.name #可以直接删除实例对象中的属性（不能使用类名来删除）
#print(t.name)
#del Num.age   ##可以直接删除类中的属性类属性（必须要类名来删除）
print(Num.age)
'''
import types
#实例方法传入需要用到 函数p1.fun =types.MethodType(要添加的函数名，对象名)  对象名影响后面传入的数据，前面的只是接受
#的函数的返回值
'''
class Person(object):
    def __init__(self,newName):
        self.name =newName


def fun(self):
    print('----%s找死----'%self.name)
p1 =Person('老王')
p1.fun =types.MethodType(fun,p1)
p1.fun()
'''
#静态方法和类方法的添加
class Person(object):
    def __init__(self,newName):
        self.name =newName
@classmethod
def run(cls):
    print('---%s跑去吃屎了----'%cls.name)  #始终调用的是类属性中的值
    print('---%s跑去吃屎了----' % p1.name) #始终调用的实例对象p1中的值
@staticmethod
def fun():
    print('---%s--static  method-----'%p1.name)

p1 =Person('老王')
Person.fun =fun  #静态方法要添加到类对象里面，而不是实例对象，类方法一样
p1.fun()
Person.run =run  #类方法要添加到类对象里面，而不是实例对象
Person.name ='老张'
Person.run()
p1.run()


# 因为python是动态语言，可以任意添加属性
class Person1(object):
    __slots__ = ('name', 'age')  # 规定了只能添加的属性

    def __init__(self):
        pass


p = Person1()
p.age = 20
p.name = 'laowang'
#p.num = 222  # 不能添加 num属性