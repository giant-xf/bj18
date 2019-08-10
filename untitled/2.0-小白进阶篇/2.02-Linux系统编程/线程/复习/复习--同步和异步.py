from threading import Thread,Lock
from time import sleep


# 线程的同步
# class work1(Thread):
#     def run(self):
#         while True:
#             if lock1.acquire():
#                 print("----work--1--")
#                 sleep(0.5)
#                 lock2.release()
#
#
# class work2(Thread):
#     def run(self):
#         while True:
#             if lock2.acquire():
#                 print("----work--2--")
#                 sleep(0.5)
#                 lock3.release()
#
# class work3(Thread):
#     def run(self):
#         while True:
#             if lock3.acquire():
#                 print("----work--3--")
#                 sleep(0.5)
#                 lock1.release()
#
#
# if __name__ == '__main__':
#     lock1 = Lock()
#
#     lock2 = Lock()
#     lock2.acquire()
#
#     lock3 = Lock()
#     lock3.acquire()
#
#     t1 = work1()
#     t2 = work2()
#     t3 = work3()
#
#     t1.start()
#     t2.start()
#     t3.start()


#线程的异步
from multiprocessing import Pool
import time
import os
def test():
    print("---进程池中的进程---pid=%d,ppid=%d--"%(os.getpid(),os.getppid()))
    for i in range(3):
        print("----%d---"%i)
        time.sleep(1)
    return "hahah"
def test2(args):
    print("---callback func--pid=%d"%os.getpid())
    print("---callback func--args=%s"%args)


if __name__ == '__main__':

    pool = Pool(3)
    pool.apply_async(func=test,callback=test2)

    #主线程自己做自己的事，然后等子线程结束后再调用主线程做别的事
    #(子线程什么时候做完不固定，主线程边做自己的事边等待)
    while True:
        time.sleep(0.5)
        print("----主进程-pid=%d----"%os.getpid())

