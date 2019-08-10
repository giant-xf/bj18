class Store(object):
    def  select_car(self):
        pass
    def order(self,car_type):
        return self.select_car(car_type)
class Car(object):
    def move(self):
        print('车在移动------')
    def music(self):
        print('正在放歌------')
    def stop(self):
        print('车正在停车----')

class BMWStore(Store):
    def select_car(self,car_type):
        return BMWFactory().selet_car_type(car_type)
class BMWFactory(object):
    def selet_car_type(self, car_type):
        if car_type == 'mini':
            return Mini()
        elif car_type == 'X6':
            return X6()
class Mini(Car):
    def print_type(self):
        print('我是Mini')
class X6(Car):
    def print_type(self):
        print('我是X6')

class CarStore(Store):
    #def __init__(self):
        #self.factory =Factory()
    #def order(self,car_type):
        #return Factory().selet_car_type(car_type)
    def select_car(self,car_type):
        return Factory().selet_car_type(car_type)
class Factory(object):
    def selet_car_type(self,car_type):
        if car_type == '索纳塔':
            return Suonata()
        elif car_type == '名图':
            return Mingtu()
class Suonata(Car):
    def print_type(self):
        print('我是Suonata')
class Mingtu(Car):
    def print_type(self):
        print('我是Mingtu')

if __name__ == '__main__':
    car_Store =CarStore()
    car =car_Store.order('索纳塔')
    car.print_type()
    car.move()
    car.music()
    car.stop()
    car_Store1 =BMWStore()
    car1 =car_Store1.order('X6')
    car1.print_type()
    car1.move()
    car1.music()
    car1.stop()
