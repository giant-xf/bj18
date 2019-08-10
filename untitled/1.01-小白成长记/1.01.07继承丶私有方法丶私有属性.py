
'''class  People(object):
    def __init__(self,name):
        self.__name  =name
        self.Name  =name
    def  getName(self):
        return self.__name

    def setName(self,new_name):
        if len(new_name)>=5:
            self.__name =new_name
        else:
            print('error : 名字长度必须大于4,')

#初始化
xiaowang =People('fengge')
print(xiaowang.getName())
xiaowang.setName('wangge')
print(xiaowang.getName())
xiaowang.setName(('lisi'))
print(xiaowang.getName())
print(xiaowang.Name)
'''
#单例继承
'''class  Cat(object):
    count  =None
    def __init__(self,new_name,new_color):
        self.name =new_name
        self.color =new_color

    def run(self):
        print('%s的%s在----跑----'%(self.color,self.name))
    #重写__new__方法  实现单例模式
    def __new__(cls, *args, **kwargs):
        if cls.count ==None:
            cls.count =object.__new__(cls)
            return cls.count
            count  +=1
        else :
            return cls.count

class Bosimao(Cat):
    def eat(self):
        print('%s的%s--在吃东西---'%(self.color,self.name))

    def set_name(self,new_name):
        self.name =new_name
    def set_color(self,new_color):
        self.color =new_color
bsm =Cat('印度猫','白色')
#print(id(bsm))
bsm.run()
#bsm.set_name('波斯猫')
#bsm.set_color('红色')
#bsm.eat()
bsm.run()
bsm1 =Cat('','')
#print(id(bsm1))

bsm1.run()'''
#私有属性及私有方法
''''class Animal(object):
    def __init__(self,name ='小狗',color  ='白色'):
        self.__name =name
        self.color  =color

    def __test(self):
        print(self.__name)
        print(self.color)

    def test(self):
        print(self.__name)
        print(self.color)

    #无法直接访问，只能在父类中定义一个方法来调用私有属性或者私有方法
    def print_test(self):
        self.__test()

class Dog(Animal):
    def Dogtest(self):
        #self.__test()       #不能访问
        #self.__name       #不能访问
        self.test()
dog =Dog(name='小黄',color='绿色')
dog.Dogtest()
dog.print_test()'''
