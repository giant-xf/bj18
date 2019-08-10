class f(object):
    def __getattribute__(self, item):
        print('----',item)
        if item =='a':
            print('------>',item)
            return "python"

        else:
            # 不允许再调用self.b函数，否则进入死循环
            return object.__getattribute__(self,item)

    def b(self):
        print( 'test')

c =f()

print(c.a)
c.b()

#总结：在Python对象中，没有函数，保存的都是属性，
# 当访问属性或者方法时，都是先调用__getattribute__方法，对象中只存储属性，
#   属性引用外部的函数，所以之前Person.testClass = testClass给类添加类方法等等
#   都是一样的道理，仅仅只是添加了一个属性。然后属性指向这个函数