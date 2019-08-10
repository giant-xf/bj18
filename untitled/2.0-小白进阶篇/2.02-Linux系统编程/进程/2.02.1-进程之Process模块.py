#windows上面使用进程用的multiprocessing模块
# os.fork()  只能在Linux丶mac 上面使用
'''
Process([group [, target [, name [, args [, kwargs]]]]])
    target：表示这个进程实例所调⽤对象；
    args：表示调⽤对象的位置参数元组；
    kwargs：表示调⽤对象的关键字参数字典；
常用方法:
    start()：启动进程实例（创建⼦进程）；
    join([timeout])(阻塞)：是否等待进程实例执⾏结束，或等待多少秒；
    terminate()：不管任务是否完成，⽴即终⽌；
常用属性:
    pid：当前进程实例的PID值；
'''
#Process模块
#主进程先等待子进程先结束，然后再结束
from multiprocessing import Process
from multiprocessing import Pool
from multiprocessing import Queue
import time
import os
import random
#进程函数
def person(name):
    for i in range(2):                          #子进程的PID  #父进程的PID
        print('----子进程%s--%d--%d---'%(name,os.getpid(),os.getppid()))
        time.sleep(random.random())
if __name__ =='__main__':
    p =Process(target=person,args=('person',))
    p.start()
    for i in range(2):               #父进程的PID
       print('---主进程%d---%d-'%(os.getpid(),os.getppid()))
       time.sleep(random.random())

    p.join()
    print('over')


#创建进程类
class Person_Class(Process):
    def __init__(self,time_):
        Process.__init__(self)
        self.time =time_

    def run(self):
        for i in range(4):
            print('-------1-------')
            time.sleep(self.time)

if __name__ =='__main__':
    p =Person_Class(1)
    #调用父类Process中start()方法，实现run()方法
    #与简单工程模式类似
    p.start()
    for i in range(2):
        print('----main-----')
        time.sleep(1)
    p.join()
    print('---over----')


