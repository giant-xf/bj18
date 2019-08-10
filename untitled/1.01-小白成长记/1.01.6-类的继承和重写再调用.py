class Animal(object) :
    def  eat(self):
        print('-----吃-----')
    def drink(self):
        print('-----喝-----')
    def sleep(self):
        print('-----睡觉-----')
    def run(self):
        print('-----跑-----')
    def bark(self):
        print('----鬼叫-----')
class Dog(Animal) :
    def  bark(self):
        print('-----汪汪叫-----')
class Xiaotq(Dog):
    def fly(self):
        print('-----飞-----')
    def bark(self):
        print('-----狂叫-----')
        #调用被重写的1方法
        #第一种方法
        #Dog.bark(self)
            #可以调用父类的父类
        #Animal.bark(self)
        #第二种方法
        super().bark()
xiaotq =Xiaotq()
xiaotq.fly()
xiaotq.bark()
xiaotq.eat()