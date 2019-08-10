#python采⽤的是引⽤计数机制为主和分代回收为辅的策略

#1、查看⼀个对象的引⽤计数
import sys
import gc

a = "hello world"
print(sys.getrefcount(a))



class ClassA():
    def __init__(self):
        print('object born,id:%s'%str(hex(id(self))))
def f2():
    while True:
        c1 = ClassA()
        c2 = ClassA()
        c1.t = c2
        c2.t = c1
        del c1
        del c2
#把python的gc关闭
gc.disable()
f2()

# 注意点
# gc模块唯⼀处理不了的是循环引⽤的类都有__del__⽅法，所以项⽬中要避免
# 定义__del__⽅法


# 有三种情况会触发垃圾回收：
# 1. 调⽤gc.collect(),
# 2. 当gc模块的计数器达到阀值的时候。
# 3. 程序退出的时候
