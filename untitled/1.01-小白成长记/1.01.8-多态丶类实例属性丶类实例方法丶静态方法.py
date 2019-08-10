#多态
'''class Dog(object):
    def test(self):
        print('我是text')

class Xtq(Dog):
    def test(self):
        print('我是哮天犬，我是老大')

#多态的体现   
def introduce(temp):
    temp.test()
xtq =Xtq()
dog =Dog()
introduce(dog)'''
#类属性和实例属性，类对象和实例对象
'''class People(object):
    count = 'china'
    def getname(self):
        self.name ='小白'
a =People()
b =People()

#类对象丶类对象都能引用类属性的值   仅仅只有类对象引用时才会修改类属性的值
#l类对象无法访问实例属性的值
a.count ='japen' #自动创建了一个实例属性
print(a.count)      #实例属性会强制屏蔽掉同名的类属性
print(b.count)      #并不会修改类属性的值
del a.count  #只有删除了以后才能继续引用类属性的值
print(a.count)
People.count ='USA' #只有类对象引用了类属性才能修改类属性的值
print(People.count)
#print(People.name)  #会报错，类对象无法引用实例对象的实例属性
'''
#类方法丶实例方法和静态方法
'''
#类方法可以修改类属性,
#类方法可以用类对象引用，也可以用实例对象引用
class Game(object):
    num =0
    def __init__(self,name):
        self.__name =name

    #实例方法操作实例属性
    def getname(self):
        return (self.__name)

    #类方法操作类属性
    @classmethod
    def  ch_num(cls):
        Game.num=100
        #cls.num =100
    #与其他无关，可以用静态方法
    @staticmethod
    def print_menu():
        print('----------')
        print('静态方法')
        print('----------')
game =Game('laowang')
Game.ch_num()      #可以用类对象直接调用类方法
print(Game.num)#类对象去调用类属性
game.ch_num()       #也可以用实例对象直接调用类方法
print(game.num)#实例对象去调用类属性
print(game.getname())
#Game.print_menu()      #可以用类对象调用静态方法
game.print_menu()       #可以用实例对象直接调用静态方法
'''