from threading import Thread,Lock
import time,threading


#多线程-共享全局变量
# num =0
# def work1():
#     global num
#     for i in range(100):
#         num +=1
#     print('----work1---num=%d'%num)
#
# def work2():
#     global num
#     print('----work2---num=%d'%num)
#
# if __name__ == '__main__':
#     print('线程创建之前的num值为: %d'%num)
#
#     t1 =Thread(target=work1())
#     t1.start()
#
#     #保证t1线程中的事先做完
#     time.sleep(1)
#
#     t2 =Thread(work2())
#     t2.start()


#列表当做实参传递到线程中(可变数据类型)
# def work1(nums):
#     nums.append(44)
#     print("----in work1---",nums)
#
# def work2(nums):
#     #延时⼀会，保证t1线程中的事情做完
#     time.sleep(1)
#     print("----in work2---",nums)
# if __name__ == '__main__':
#
#     g_nums = [11,22,33]
#     t1 = Thread(target=work1, args=(g_nums,))
#     t1.start()
#     t2 = Thread(target=work2, args=(g_nums,))
#     t2.start()
#总结:
# 1.在⼀个进程内的所有线程共享全局变量，能够在不适⽤其他⽅式的前提
# 2.下完成多线程之间的数据共享（这点要⽐多进程要好）
#   缺点就是，线程是对全局变量随意遂改可能造成多线程之间对全局变量
#   的混乱（即线程⾮安全）



#同步时可能遇到的问题:
#   一个全局变量，一个线程访问的时候，可能没有访问完，然后另一个变量访问了，
#   会出现第一个线程访问后第二个线程访问发现值没有改变，然后出现少加的情况
#   或者出现多减的情况(多核电脑很难体现出来，单核电脑可以体现出，结果看ubuntu)
#要想解决这个问题，把线程访问时加个Lock()锁

# num =0
# def work1():
#     global num
#
#     # True表示堵塞 即如果这个锁在上锁之前已经被上锁了，那么这个线程会在这⾥⼀直等待到解锁为⽌
        #(相当于正式上锁)
#     # False表示⾮堵塞，即不管本次调⽤能够成功上锁，都不会卡在这,⽽是继续执⾏下⾯的
        #(相当于没有上锁，不用解锁，)
#     lock.acquire()  #锁放在for循环外面效率更高，占用CPU量也更加少
#     for i in range(1000000):
#         #lock.acquire()
#         num +=1
#         #lock.release()
#     print('----work1---num=%d'%num)
#     time.sleep(1)
#     #释放锁住的状态
#     lock.release()
# def work2():
#     global num
#
#     lock.acquire()
#     for i in range(1000000):
#         #lock.acquire()
#         num +=1
#         #lock.release()
#     print('----work2---num=%d'%num)
#     time.sleep(1)
#     lock.release()
# if __name__ == '__main__':
#
#     print('线程创建之前的num值为: %d'%num)
#
#     # 创建⼀个互斥锁
#     # 这个所默认是未上锁的状态
#     lock = Lock()
#     tt1 =time.time()
#     t1 =Thread(target=work1())
#     t2 =Thread(target=work2())
#
#
#     #保证t1线程中的事先做完
#     #time.sleep(1)
#     t2.start()
#     t1.start()
#     tt2 =time.time()
#     print('--time =%.3f--num =%d'%((tt2-tt1),num))
# #总结:
# # 上锁解锁过程
# # 当⼀个线程调⽤锁的acquire()⽅法获得锁时，锁就进⼊“locked”状态。
# # 每次只有⼀个线程可以获得锁。如果此时另⼀个线程试图获得这个锁，该线
# # 程就会变为“blocked”状态，称为“阻塞”，直到拥有锁的线程调⽤锁的
# # release()⽅法释放锁之后，锁进⼊“unlocked”状态。
# # 线程调度程序从处于同步阻塞状态的线程中选择⼀个来获得锁，并使得该线
# # 程进⼊运⾏（running）状态。





#局部变量不共享
#1.不同函数之间的多个线程不共享局部变量
# class MyThread(Thread):
#     def __init__(self,num,sleeptime):
#         Thread.__init__(self)
#         self.num =num
#         self.sleeptime =sleeptime
#
#     def run(self):
#         self.num +=1
#         time.sleep(self.sleeptime)
#         print('线程(%s),num=%d'%(self.name,self.num))
#
# if __name__ == '__main__':
#     lock =Lock()
#     t1 =MyThread(100,0)
#     t1.start()
#     t2 =MyThread(200,0)
#     t2.start()
#
#同一个函数的多个线程之间不共享局部变量
# def MyThread():
#     name  =threading.current_thread().name
#     num=100
#     if name =='Thread-1':
#         num += 1
#     else:
#         time.sleep(1)
#     print('---(%s)--num=%d'%(name, num))
#
# t1 = Thread(target=MyThread)
# t2 = Thread(target=MyThread)
#
# t1.start()
# t2.start()



#ThreadLocal:
#   在多线程环境下，每个线程都有⾃⼰的数据。⼀个线程使⽤⾃⼰的局部变量
#   ⽐使⽤全局变量好，因为局部变量只有线程⾃⼰能看⻅，不会影响其他线
#   程，⽽全局变量的修改必须加锁。

    # 创建全局ThreadLocal对象:
# local_school =threading.local()
#
# def process_student():
#     std =local_school.name
#     print('hello  %s (in %s)'%(std,threading.current_thread().name))
#
# def process_thread(name):
#     local_school.name =name #两个线程传入两个值，互不影响
#     process_student()
#
# t1 =Thread(target=process_thread,args=('fengge',),name='Thread-A')
# t2 =Thread(target=process_thread,args=('laowang',),name='Thread-B')
# t1.start()
# t2.start()
# t1.join()
# t2.join()
