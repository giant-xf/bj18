class Car(object):
    #初始化
    def __init__(self,name):
        self.name=name
        self.color="黑色"
        self.wheelNum=4

    def __str__(self):
        msg ='嗨喽...我的颜色是'+self.color+"我名字叫做"+self.name
        return msg

    #移动
    def move(self):
        print("%s%s车在移动———"%(self.color,self.name))

    #鸣叫
    def toot(self):
        print("%s车在鸣笛———"%self.name)

BMW =Car("BWM")
BMW.move()
BMW.toot()
print(BMW)

#烤地瓜了类
class SweetPotato(object):
    '这是地瓜类'

    def __init__(self):
        self.cookedLevel =0
        self.cookedString ='生的'
        self.condiments =[]

    def __str__(self):
        msg =self.cookedString+'地瓜'
        if len(self.condiments)>0:
            msg =msg+'('

            for temp in self.condiments:
                msg =msg+temp+','
            msg =msg.strip(",")
            msg =msg+')'
        return msg

    def cook(self,time):
        self.cookedLevel+=time

        if self.cookedLevel>8:
            self.cookedString ='烤成黑炭了'

        elif self.cookedLevel>5:
            self.cookedString ='烤好了'

        elif self.cookedLevel>3:
            self.cookedString ="半生不熟"

        else:
            self.cookedString ='生的'

    def addconditems(self,conditems):
        self.condiments.append(conditems)


sw =SweetPotato()
sw.cook(3)
print(sw)
sw.cook(3)
sw.addconditems("芥末")
print(sw)
sw.cook(3)
sw.addconditems("辣椒")
print(sw)


#存放家具
class Home(object):
    '家的类'

    def __init__(self,area):
        self.area = area#房间的剩余可用面积
        self.containsItem = [] #房间存放的家具

    def __str__(self):
        msg ='当前房间可用面积为:'+str(self.area)

        if len(self.containsItem)>0:
            msg = msg + '('
            msg = msg + '容纳的物品有:'
            for temp in self.containsItem:
                msg = msg + temp.getname() +','
            msg =msg + ")"
            msg =msg.strip(',')
        return msg


    #存放物品的方法
    def add_jiaju(self,item):
        needArea =item.getUsearea()
        if self.area> needArea:
            self.containsItem.append(item)
            self.area-=needArea
            print('存放成功-----')
        else:
            print("你所存的床面积大于剩余房间面积，存储失败")

class bed(object):
    '床的类'
    def __init__(self,area,name='床'):
        self.area = area
        self.name = name

    def __str__(self):
        msg = "床的面积为:"+str(self.area)
        return msg

    def getUsearea(self):
        return self.area

    def getname(self):
        return self.name

xms = bed(9,'席梦思')
da =bed(19,'大床')
print(xms)
home =Home(100)
print(home)
home.add_jiaju(xms)
print(home)
home.add_jiaju(da)
print(home)


#私有方法：
class People(object):

    def __init__(self,name):
        self.__name =name

    def getName(self):
        return self.__name

    def setName(self,newname):
        if len(newname)>5:
            self.__name =newname

        else:
            print("error: 名字太短")

xiaowang=People('xxx')
xiaowang.setName("xiaowang")
print(xiaowang.getName())
xiaowang.setName("xias")
print(xiaowang.getName())



#多继承时方法相同-----采用广度遍历
class base(object):
    def test(self):
        print("--base  test---")


class A(base):
    def test(self):
        print('--A  test')


class B(base):
    def test(self):
        print("--B  test")


class C(A,B):
    pass

c =C()
c.test()
print(C.__mro__)


#多态
class f(object):
    def show(self):
        print("f.show")

class s1(f):
    def show(self):
        print('s1.show')

class s2(f):
    def show(self):
        print('s2.show')

def fun(obj):
    return obj.show()


ff =s1()
fun(ff)



#模拟4S店
#创建一个伊兰特车工厂
class YilanteCar(object):

    #定义类的方法
    def move(self):
        print("----车在移动")

    def stop(self):
        print("----停车")

#创建索拉塔车工厂
class SuolataCar(object):
    def __init__(self,typename):
        self.typename =typename

    def __str__(self):
        return ("恭喜买了一辆索拉塔")

    def move(self):
        print(self.typename+"车在移动")

    def stop(self):
        print(self.typename+'----停车')

class CarFactory(object):
    def createCar(self,typename):
        if typename =='伊兰特':
            car =YilanteCar(typename)

        elif typename =='索拉塔':
            car =SuolataCar(typename)

        return  car

#定义一个卖车4S店
class Carstore(object):
    def __init__(self):
        self.carFactory =CarFactory()

    def order(self,carname):
        car =self.carFactory.createCar(carname)
        return car


car =Carstore()
suolatacar =car.order('索拉塔')
print(suolatacar)
suolatacar.move()
suolatacar.stop()

#多个4S店
#创建一个伊兰特车工厂
class YilanteCar(object):

    #定义类的方法
    def move(self):
        print("----车在移动")

    def stop(self):
        print("----停车")

#创建索拉塔车工厂
class SuolataCar(object):
    def __init__(self,typename):
        self.typename =typename

    def __str__(self):
        return ("恭喜买了一辆索拉塔")

    def move(self):
        print(self.typename+"车在移动")

    def stop(self):
        print(self.typename+'----停车')

class CarFactory(object):
    def createCar(self,typename):
        if typename =='伊兰特':
            self.car =YilanteCar(typename)

        elif typename =='索拉塔':
            self.car =SuolataCar(typename)

        return  self.car

#定义一个卖车4S店
class Carstorebase(object):

    def createCar(self,typename):
        pass

    def order(self,typename):
        self.car = self.createCar(typename)
        self.car.move()
        self.car.stop()

class Xiandaicar(Carstorebase):

    def createCar(self,typename):
        self.carFactory =CarFactory()
        return self.carFactory.createCar(typename)

suolata =Xiandaicar()
suolata.order('索拉塔')










