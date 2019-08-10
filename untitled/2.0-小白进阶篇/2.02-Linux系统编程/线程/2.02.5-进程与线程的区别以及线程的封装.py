#1.多个进程没有先后顺序，线程是CPU调度和分派的基本单位，而进程是系统进⾏资源分配和调度的⼀个独⽴单位.
#2.主线程是等待所有子线程结束了才结束，否则出现(僵尸线程，孤儿线程)
#3.所以的进程都由pid为1的进程直接或者间接创建
#4.进程是活的，程序是死的，进程 > 线程,在进程中可以有多个线程，所有线程共享全局变量，进程不会
#   ⼀个程序⾄少有⼀个进程,⼀个进程⾄少有⼀个线程.
#5.线程Thread(target=函数名,args=(q,),name =' ')与进程的process(target=函数名,args=(q,))相同的用法
#6.线程和进程需要start()开启(进程池不需要，但是需要关闭close())
# 区别
# 1.⼀个程序⾄少有⼀个进程,⼀个进程⾄少有⼀个线程.
# 2.线程的划分尺度⼩于进程(资源⽐进程少)，使得多线程程序的并发性⾼。
# 3.进程在执⾏过程中拥有独⽴的内存单元，⽽多个线程共享内存，从⽽极⼤地提⾼了程序的运⾏效率
# 4.线线程不能够独⽴执⾏，必须依存在进程中
# 5.线程中GIL的问题，使得进程的效率比线程快，线程不能同时在多核中执行，进程可以
#   GIL问题需用C语言来解决
#线程和进程在使⽤上各有优缺点:线程执⾏开销⼩，但不利于资源的管理和保护；⽽进程正相反。

from threading import Thread
import time,threading

#多线程执⾏的同步性
# def saySorry(count):
#     print("这是线程【%d】在运行"%count)
#     #在这里睡眠没有作用，五个线程同步进行，
#     time.sleep(1)
# if __name__ == "__main__":
#     for i in range(5):
#         t = Thread(target=saySorry,args=(i,))
#         t.start()  # 启动线程，即让线程开始执⾏
#

#线程执⾏代码的封装
# class MyThread(Thread):
#     def run(self):
#         for i in range(5):
#             #time.sleep(1)

#             msg ="I'M"+self.name+'@'+str(i)
#             print(msg)
#
#
# if __name__ == '__main__':
#     t =MyThread()
#     t2 =MyThread()
#     t2.start()
#     t.start()
# 总结
# 1. 每个线程⼀定会有⼀个名字，尽管上⾯的例⼦中没有指定线程对象的
#     name，但是python会⾃动为线程指定⼀个名字。
# 2. 当线程的run()⽅法结束时该线程完成。
# 3. ⽆法控制线程调度程序，但可以通过别的⽅式来影响线程调度的⽅式。
# 4. 线程的⼏种状态
#新建---->>就绪<---->运行----->死亡
 #             等待(阻塞)
''' 
python的threading.Thread类有⼀个run⽅法，⽤于定义线程的功能函
数，可以在⾃⼰的线程类中覆盖该⽅法。⽽创建⾃⼰的线程实例后，通
过Thread类的start⽅法，可以启动该线程，交给python虚拟机进⾏调
度，当该线程获得执⾏的机会时，就会调⽤run⽅法执⾏线程。
'''






#查看线程数量,计算主线程和子线程同时运行
def sing():
    for i in range(3):
        print("正在唱歌...%d"%i)
        time.sleep(1)

def dance():
    for i in range(3):
        print("正在跳舞...%d"%i)
        time.sleep(1)

if __name__ == '__main__':
    print('----开始------%s'%time.ctime())

    t1 =Thread(target=sing)
    t2 =Thread(target=dance)

    t1.start()
    t2.start()

    while True:
        length =len(threading.enumerate())
        print('当前运行的线程数为: %d'%length)
        if length==1:
            break

        time.sleep(0.5)


