import threading
import time
#python2中
#from Queue import Queue
#python3中
from queue import Queue

#一.使用多线程实现生产者与消费者模型(锁(Lock)模型丶Condit(条件)模型丶Queue(队列)模型丶信号量模型丶Event(事件)模型)
    #1. Queue(队列)模型
class Producer(threading.Thread):
    def run(self):
        global queue
        count = 0
        while True:
            if queue.qsize() < 1000:
                for i in range(10):     #多个线程同时执行，会出现相同的数字但是在取出来的时候不影响
                    count = count + 1
                    msg = '⽣成产品' + str(count)
                    queue.put(msg)
                    print(msg)
            time.sleep(0.5)    #若生产量大于消费量，且出现滞销时，暂停生成时间

class Consumer(threading.Thread):
    def run(self):
        global queue
        while True:
            if queue.qsize() > 100:
                for i in range(30):
                    msg = self.name + '消费了 ' + queue.get()
                    print(msg)
            time.sleep(1)       #若消费量大于生成量，且出现没有货时，暂停消费
if __name__ == '__main__':
    queue = Queue()
    for i in range(1,501):
        queue.put('初始产品' + str(i))
    for i in range(2):
        p = Producer()
        p.start()
    for i in range(5):
        c = Consumer()
        c.start()
    print(queue.qsize())


#二.多进程实现生产者与消费者模型(信号量和共享内存丶Condition模型丶消息队列模型丶管道(Pipe)模型丶Event模型)




#三。不同主机上生产者消费者模型（socketTCP模型丶远程调用(RPC)模型）
