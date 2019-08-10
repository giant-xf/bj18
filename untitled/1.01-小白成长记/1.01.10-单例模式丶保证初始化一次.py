class Game(object):
    count  =None
    name ='CF'
    count_flag=True

    #def  setname(self,name):
    #    self.name =name
    def __new__(cls, *args, **kwargs):
        if cls.count ==None:
            cls.count =object.__new__(cls) #引用object创建对象
            return  cls.count
        else:
            return cls.count
    def  __init__(self,name):
        #保证只初始化一次
        if self.count_flag :
            self.count_flag =False
            self.name =name
#a =Game()
#a.setname('DNF')
#print(a.name)
#b  =Game()
#print(b.name) #此时两个对象都引用一个，所以此时修改了a实例对象的name,那么b实例对象引用的name也变化了
#print(Game.name)
a =Game('旺财')
print(a.name)
b =Game('哮天犬')
print(b.name)
c =Game('22222')
print(c.name)