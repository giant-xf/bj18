'''
xx: 公有变量
_x: 单前置下划线（包括__xx）,私有化属性或⽅法，from somemodule import *禁⽌导
    ⼊类对象和⼦类可以访问，但是可以import导入
__xx：双前置下划线,避免与⼦类中的属性命名冲突，⽆法在外部直接访
    问(名字重整所以访问不到)
__xx__:双前后下划线,⽤户名字空间的魔法对象或属性。例
    如: __init__ , __ 不要⾃⼰发明这样的名字
xx_:单后置下划线,⽤于避免与Python关键词的冲突，无法访问的私有属性__xx(相当于名字重整为_Class__xx):

通过name mangling（名字重整(⽬的就是以防⼦类意外重写基类的⽅法或者
属性)如：_Class__object）机制就可以访问private了。

'''

#property的第一种用法
class Num(object):
    def __init__(self):
        self.__num =10

    def setnum(self,new_num):
        self.__num=new_num

    def getnum(self):
        return self.__num

    num =property(getnum,setnum)
p=Num()
#p.__num =200  #相当于在对象中新创建了个__num属性，并非修改了原有的私有属性__num
#p.setnum(200)
#print(p.getnum())
p.num =200
print(p.num)
print('-'*30)
#property的第二种用法
class Money(object):
    def __init__(self):
        self.__money =10

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self,new_money):
        self.__money =new_money

p =Money()
p.money =20
print(p.money)
