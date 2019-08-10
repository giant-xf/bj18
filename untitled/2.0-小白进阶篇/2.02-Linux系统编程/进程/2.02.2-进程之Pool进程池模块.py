from multiprocessing import Pool,Manager
import time
import os
import random
#Pool模块
#主进程没有运行的程序会自动结束，不会等待子程序再结束，
# def worker(num):
#     for  i in range(5):
#         print('----PID=%d---num=%d'%(os.getppid(),num))
#         time.sleep(1)
#
#
# #进程必须使用这个测试
# if __name__ =='__main__':
#     #3表示进程池最多只能3个进程一起进行
#     po =Pool(3)
#     #向进程中添加进程任务
#     #注意:如果添加的任务数量大于进程池最大值，不会出现添加
#     #      不进去的现象,只先同时执行3个，其他任务进入等待状态
#     #       等待进程池中的进程完成，然后再自动执行等待中的进程
#     #       多个进程不能同时进行一个任务
#     for  i in range(7):
#         print('---%d---'%i)
#                               #以元组的方式传入参数
#         po.apply_async(worker,(i,))
#
#     po.close()  #关闭进程池，不能再继续添加进程到进程池
#     po.join()   #主进程完成  创建/添加  的任务后，主进程默认
#                 # 不会等待子进程结束再结束，而是没有任务后自动结束
#                 # 那么主进程结束以后，子进程也会结束，所以必须进入
#                 #阻塞状态，使主进程等待子进程结束再结束
#
#

def read(q):
    print('read启动(%s)，父进程(%s)'%(os.getpid(),os.getppid()))
    for i in range(q.qsize()):
        print('read从Queue获取到消息:%s'%q.get(True))
        time.sleep(random.random())

def write(q):
    print('write启动(%s),父进程(%s)'%(os.getpid(),os.getppid()))
    for i in  ['A','B','C','D']:
        q.put(i)
        print('write到Queue保存的消息:%s'%(i))
        time.sleep(random.random())
    print('传入完成')
    #time.sleep(2)
if __name__ =='__main__':
    print('%s----start'%os.getpid())
    q =Manager().Queue()
    po =Pool()
    po.apply(write,(q,))
    po.apply(read,(q,))
    po.close()
    po.join()
    print('%s----END'%os.getpid())


