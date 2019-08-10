from multiprocessing import Queue,Process,Pool
from multiprocessing import Manager
import time
import os
import random
'''
Queue.qsize()：返回当前队列包含的消息数量；
Queue.empty()：如果队列为空，返回True，反之False ；
Queue.full()：如果队列满了，返回True,反之False；
Queue.get([block[, timeout]])：获取队列中的⼀条消息，然后将其从列队
    中移除，block默认值为True；
    1）如果block使⽤默认值，且没有设置timeout（单位秒），消息列队如果为
    空，此时程序将被阻塞（停在读取状态），直到从消息列队读到消息为⽌，
    如果设置了timeout，则会等待timeout秒，若还没读取到任何消息，则抛
    出"Queue.Empty"异常；
    2）如果block值为False，消息列队如果为空，则会⽴刻抛
    出"Queue.Empty"异常；
Queue.get_nowait()：相当Queue.get(False)；
Queue.put(item,[block[, timeout]])：将item消息写⼊队列，block默认值
    为True；
    1）如果block使⽤默认值，且没有设置timeout（单位秒），消息列队如果已
    经没有空间可写⼊，此时程序将被阻塞（停在写⼊状态），直到从消息列队
    腾出空间为⽌，如果设置了timeout，则会等待timeout秒，若还没空间，则抛
    出"Queue.Full"异常；
    2）如果block值为False，消息列队如果没有空间可写⼊，则会⽴刻抛
    出"Queue.Full"异常；
Queue.put_nowait(item)：相当Queue.put(item, False)；
'''

#Process进程间的通信 使用Queue()就行

# q=Queue(3) #初始化⼀个Queue对象，最多可接收三条put消息
# q.put("消息1")
# q.put("消息2")
# print(q.full()) #False
# q.put("消息3")
# print(q.full()) #True
# #因为消息列队已满下⾯的try都会抛出异常，，
# try:
#     q.put("消息4",True,2) #第⼀个try会等待2秒后再抛出异常
# except:
#     print("消息列队已满，现有消息数量:%s"%q.qsize())
# try:
#     q.put_nowait("消息4")##⼆个Try会⽴刻抛出异常
# except:
#     print("消息列队已满，现有消息数量:%s"%q.qsize())
# #推荐的⽅式，先判断消息列队是否已满，再写⼊
# if not q.full():
#     q.put_nowait("消息4")
# #读取消息时，先判断消息列队是否为空，再读取
# if not q.empty():
#     for i in range(q.qsize()):
#         print(q.get_nowait())

#process进程之间的通信
# 写数据进程执⾏的代码:
# def write(q):
#     for value in ['A', 'B', 'C']:
#         print( 'Put %s to queue...' % value)
#         q.put(value)
#         time.sleep(random.random())
#     # 读数据进程执⾏的代码:
# def read(q):
#     while True:
#         if not q.empty():
#             value = q.get(True)
#             print('Get %s from queue.' % value)
#             time.sleep(random.random())
#         else:
#             break
# if __name__=='__main__':
#     # ⽗进程创建Queue，并传给各个⼦进程：
#     q = Queue()
#     pw = Process(target=write, args=(q,))
#     pr = Process(target=read, args=(q,))
#     # 启动⼦进程pw，写⼊:
#     pw.start()
#     # 等待pw结束:
#     #pw.join()
#     # 启动⼦进程pr，读取:
#     pr.start()
#     pr.join()
#     # pr进程⾥是死循环，⽆法等待其结束，只能强⾏终⽌:
#     print ('\n所有数据都写⼊并且读完')
#


#Pool进程池中的通信需要调用Manager().Queue() 才行
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
    po.apply(write,(q,))  #阻塞，防止其他进程占用
    po.apply(read,(q,))
    #po.apply_async(write,(q,))
    #po.apply_async(read,(q,))
    po.close()
    po.join()

    print('%s----END'%os.getpid())


