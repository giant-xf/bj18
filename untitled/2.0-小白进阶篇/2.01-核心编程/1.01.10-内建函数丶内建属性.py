#import pdb
#pdb.set_trace()  #设置断点调试


#内建属性
'''
不仅可以拦截属性，还可以拦截方法
'''

class Itcast(object):
    def __init__(self,subject1):
        self.subject1 =subject1
        self.subject2 ='cpp'
        # 属性访问时拦截器
    def __getattribute__(self,item):
        if item =='subject1':   #拦截属性
            print('log  subject1')
            return  'redirect  python'
        else:   #测试时注释掉这2⾏，将找不到subject2
            return object.__getattribute__(self,item) #调用系统自带的__getattribute__方法
            #return self.show #不能返回self.xxx类型的，否则会死循环
            #return  '666'
    #方法也可以拦截
    def show(self):
        print('this is show')

s =Itcast('python')
print(s.subject1)
print(s.subject2)
s.show()    #拦截方法

#内建属性的坑
class Person(object):
    def __getattribute__(self, item):
        print('---show---')
        if  item.startswith('a'):
            return 'hhhhh'
        else:
            return  self.show  # 注意：以后不要在__getattribute__⽅法中调⽤self.xxxx

    def show(self):
        print('hehehehe')

p =Person()
print(p.a)
#p.b  #会使程序死掉




