class Home(object):
    def __init__(self,new_area,new_info,new_addr):
        self.area =new_area
        self.info =new_info
        self.addr =new_addr
        self.left_area =new_area
        self.contain_items =[]
    def __str__(self):
        msg ='房子的总面积为%d，剩余可用面积为%d，户型为%s,'%(self.area,self.left_area,self.info)
        #return ('房子的总面积是%d,剩余可用面积为%d，户型是%s，地址是%s,里面家具有%s'%(self.area,self.left_area,self.info,self.addr,str(self.contain_items)))
        msg +='地址为%s,房间物品有:('%(self.addr)
        for temp in self.contain_items:
            msg =msg +temp+','
        msg =msg.strip(',')
        msg +=')'

        return msg
    def add_item(self,item):
        #方法一访问Bed 类的内部   不提倡
        #self.left_area -=item.area
        #self.contain_items.append(item.name)
        #方法二访问Bed类中的输出函数   提倡
        #self.left_area  -=item.get_area()
        if self.left_area>=item.get_area():
            self.contain_items.append(item.get_name())
            self.left_area -=item.get_area()
        else:
            print('error :房间位置不足，无法放入该物品')
class Bed(object):
    def __init__(self,new_name,new_area):
        self.name = new_name
        self.area  =new_area

    def __str__(self):
        return ('%s占面积为%d'%(self.name,self.area))

    def get_area(self):
        return self.area

    def get_name(self):
        return self.name

class TV(object):
    def __init__(self,new_name,new_area):
        self.name =new_name
        self.area =new_area

    def __str__(self):
        return "%s占地面积为%d"%(self.name,self.area)

    def get_name(self):
         return self.name

    def get_area(self):
        return self.area

class Yugang(object):
    def __init__(self,new_namem,new_area):
        self.area =new_area
        self.name =new_namem

    def __str__(self):
        return "%s占地面积为%d"%(self.name,self.area)

    def get_name(self):
         return self.name

    def get_area(self):
        return self.area

if __name__ == '__main__':
    fangzi =Home(120,'五室一厅','北京二环路666号')

    bed1  =Bed('席梦思',4)
    bed2 =Bed('三人大床',8)
    fangzi.add_item(bed1)
    print(fangzi)
    fangzi.add_item(bed2)
    print(fangzi)
    TV1 =TV('大寸网络电视',3)
    TV2 =TV('小型有线电视',2)
    TV3  =TV('投影仪',8)
    fangzi .add_item(TV1)
    fangzi.add_item(TV2)
    fangzi.add_item(TV3)
    print(fangzi)
    yugang1 =Yugang('大浴缸',8)
    fangzi.add_item(yugang1)
    print(fangzi)
    yugang2 =Yugang('洗澡喷头',300)
    fangzi.add_item((yugang2))
    print(fangzi)