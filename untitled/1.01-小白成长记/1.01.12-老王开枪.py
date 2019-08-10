
class Person(object):
    '''人物类'''
    def __init__(self,name):
        self.name =name
        self.gun =None #保存枪
        self.HP =100    #生命值

    #安装子弹到弹夹中
    def anzhuang_zidan(self,danjia_temp,zidan_temp,zidan_name):
        '''弹夹保存子弹'''
        return danjia_temp.baocun_zidan(zidan_temp,zidan_name)

    def anzhuang_danjia(self,gun_temp,danjia_temp):
        '''将弹夹安装到枪中'''
        gun_temp.baocun_danjia(danjia_temp)

    def naqiang(self,gun_temp):
        '''拿枪，存放枪'''
        self.gun  =gun_temp

        #用于输出信息
    def __str__(self):
        if self.gun:
            return '%s生命值为%d,%s'%(self.name,self.HP,self.gun)
        else:
            if self.HP>0:
                return '%s生命值为%d,没有拿枪'%(self.name,self.HP)
            else:
                return  '%s已经阵亡.....'%self.name

    def koubanji(self,diren):
        '''让枪发射子弹打敌人'''
        print('-' * 30)
        print('%s正在向%s开火'%(self.name,diren.name))

        zi_dan_temp =self.gun.kaihuo(diren)

    def diaoxue(self,sha_shang_li):
        '''根据杀伤力 敌人掉血'''
        self.HP -=sha_shang_li

class Gun(object):
    '''枪类'''
    def __init__(self,name):
        self.name =name #用来记录枪的类型
        self.danjia =None

    #将弹夹保存到枪中
    def baocun_danjia(self,danjia_temp):
        '''将弹夹保存到枪中'''
        self.danjia =danjia_temp

    def __str__(self):
        if self.danjia:
            return '枪的信息为:%s,%s'%(self.name,self.danjia)
        else:
            return '枪的信息为:%s,此时没有弹夹'%self.name

    def kaihuo(self,diren):
        '''让弹夹弹射一发子弹打敌人'''
        zidan_temp=self.danjia.fashe_zidan()
        if zidan_temp:
            #返回的子弹打中敌人
            zidan_temp.dazhong(diren)
        else:
            print('弹夹中没有子弹了..')

class Danjia(object):
    '''弹夹类'''

    def __init__(self,max_num):
        self.max_num =max_num       #弹夹的最大容量
        self.danjia_list=[]

    #将这颗子弹保存老弹夹中
    def baocun_zidan(self,zidan_temp,zidan_name):
        '''弹夹进行保存子弹'''
        #保证装的子弹不会超过容量
        if len(self.danjia_list)<self.max_num:
            self.danjia_list.append(zidan_temp)
            return True #不超过就返回True
        else:
            print('%s弹夹装满了，不能添加这么多！！最多%d颗子弹'%(zidan_name,self.max_num))
            return False #超过就返回False

    def __str__(self):
        return '弹夹的信息为:%d/%d'%(len(self.danjia_list),self.max_num)


    def fashe_zidan(self):
        '''发射最上面的那发子弹'''
        if self.danjia_list:
            return self.danjia_list.pop()
        else:
            return None

class Zidan(object):
    '''子弹类'''
    def __init__(self,sha_shang_li):
        self.sha_sahng_li =sha_shang_li     #子弹威力

        #打中敌人
    def dazhong(self,diren):
        '''打中敌人'''
        #敌人.掉血
        diren.diaoxue(self.sha_sahng_li)

class Gun_98K(Gun):
    pass
class Danjia_98K(Danjia):
    pass
class Zidan_98K(Zidan):
    pass
def main():
    """用来控制整个程序的流程"""
    pass

    #1.创建一个人物类 (老王和敌人)
   # kaiqiangren =input('请输入开枪人:')
    laowang  =Person('老王')
    #2.创建一个枪的对象
    ak47 =Gun('AK47')
    #3.创建一个弹夹对象
    dan_jia =Danjia(20) #弹夹都容量
    #4.创建一些子弹
    zi_dan =Zidan(10)   #子弹的威力
    #5.老王把子弹安装到弹夹里面
    #老王.子弹安装到弹夹里面
    #print(ak47.name)
    for j in range(30):
        if laowang.anzhuang_zidan(dan_jia,zi_dan,ak47.name):  #装子弹
            j+=1
        #若超过了20颗子弹，则返回false，终止循环，
        else :
            break

    #6.老王把弹夹安装到枪中
    #老王.弹夹安装到枪中
    laowang.anzhuang_danjia(ak47,dan_jia)

    #测试
        #测试弹夹信息
    print(dan_jia)
        #测试枪的信息
    #print(ak47)
    #7.老王拿枪
    #老王.拿枪
    laowang.naqiang(ak47)
        #测试老王的信息
    print(laowang)
    #8.创建一个敌人
    diren =Person('隔壁老宋')
        #测试敌人老宋的信息
#    print(diren)
    #9.老王开枪打敌人
    #老王.开火
    for i in range(11):
        laowang.koubanji(diren)
        print(laowang)
        print(diren)
        i+=1

if __name__ == '__main__':
    main()