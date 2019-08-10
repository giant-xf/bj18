#定义一个烤地瓜的类
class Kaodigua(object):
    #用构造函数进行初始化
    def __init__(self):
        self.cookedString ='生的'
        self.cookedLevel=0
        self.zuoliao =[]
    #用析构函数进行返回
    def __str__(self):
        return  ('地瓜的状态 %s（%d）,加入的佐料有:%s,'%(self.cookedString,self.cookedLevel,str(self.zuoliao)))
    #定义一个烤的方法
    def cook(self,cooktime):
        #将属性的时间递加，达到每次都改变
        self.cookedLevel +=cooktime
        #进行判断地瓜的状态
        if self.cookedLevel>=0 and self.cookedLevel<3:
            self.cookedString ='生的'
        elif self.cookedLevel>=3 and self.cookedLevel<5:
            self.cookedString ='半生半熟的'
        elif self.cookedLevel>=5 and self.cookedLevel<8:
            self.cookedString ='熟的'
        elif self.cookedLevel >=8:
            self.cookedString ='烤成木炭了'
    #定义一个加佐料的方法
    def add_zuoliaos(self,add_zuoliao):
        self.zuoliao.append(add_zuoliao)
#创建一个对象
di_gua =Kaodigua()

#开始烤地瓜加佐料
di_gua.cook(1)
di_gua.add_zuoliaos('大蒜')
print(di_gua)

di_gua.cook(1)
di_gua.add_zuoliaos('盐')
print(di_gua)

di_gua.cook(1)
di_gua.add_zuoliaos('老干妈')
print(di_gua)
di_gua.cook(1)
print(di_gua)
di_gua.cook(1)
di_gua.add_zuoliaos('孜然')
print(di_gua)
di_gua.cook(1)
di_gua.add_zuoliaos('辣椒粉')
print(di_gua)
di_gua.cook(1)
print(di_gua)
di_gua.cook(1)
print(di_gua)
di_gua.cook(1)
print(di_gua)

