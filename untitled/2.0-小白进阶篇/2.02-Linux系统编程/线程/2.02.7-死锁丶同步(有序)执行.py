import threading
from threading import Thread,Lock
import time

#解死锁方法:
#   1.添加超时时间
#   2.银行家算法
# class MyThread1(threading.Thread):
#     def run(self):
#         if mutexA.acquire():
#             print(self.name + '----do1---up----')
#             time.sleep(1)
#             if mutexB.acquire(True,3): #添加超时时间，等待解锁，正好
#                                         #此时MyThread2解锁了mutexB
#                 print(self.name + '----do1---down----')
#                 mutexB.release()
#             print('-------1111-----')
#             mutexA.release()
#
# class MyThread2(threading.Thread):
#     def run(self):
#         if mutexB.acquire():
#             print(self.name + '----do2---up----')
#             time.sleep(1)
#
#             if mutexA.acquire(True,1):#添加了1秒的超时时间，如果1秒后还没有解锁
#                                         #那么自动返回，执行下面的语句，成功解锁来了
#                                         #mutexB
#                 print(self.name + '----do2---down----')
#                 mutexA.release()
#             print('-------2222-----')
#             mutexB.release()
# mutexA = threading.Lock()
# mutexB = threading.Lock()
# if __name__ == '__main__':
#     t1 = MyThread1()
#     t2 = MyThread2()
#     t1.start()
#     t2.start()



#同步应⽤,多个线程有序执⾏
# class Task1(Thread):
#     def run(self):
#         while True:
#             if lock1.acquire():
#                 print('----task1----')
#                 time.sleep(0.5)
#                 lock2.release()
#
# class Task2(Thread):
#     def run(self):
#         while True:
#             if lock2.acquire():
#                 print('----task2----')
#                 time.sleep(0.5)
#                 lock3.release()
#
# class Task3(Thread):
#     def run(self):
#         while True:
#             if lock3.acquire():
#                 print('----task3----')
#                 time.sleep(0.5)
#                 lock1.release()
#
# lock1 =Lock()
#
# lock2 =Lock()
# lock2.acquire()
# lock3 =Lock()
# lock3 .acquire()
# t1 =Task1()
# t2 =Task2()
# t3 =Task3()
# t1.start()
# t2.start()
# t3.start()
