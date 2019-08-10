from multiprocessing import Process,Pool,Manager,Queue
import time,os

# def write(q):
#     for i in range(10):
#         print("put %d to Queque"%i)
#         q.put(i)
#         time.sleep(1)
#
#
# def read(q):
#     while True:
#         if not q.empty():
#             values =q.get()
#             print("get %d"%values)
#
#         else:
#             break
#
#
# if __name__ == '__main__':
#     q =Queue()
#     pw = Process(target =write,args=(q,))
#     pr = Process(target =read,args=(q,))
#     pw.start()
#     pw.join()
#     pr.start()
#     pr.join()
#     print("")
#     print("数据读完")


def reader(q):
    #print("reader启动(%s),⽗进程为(%s)"%(os.getpid(),os.getppid()))
    for i in range(q.qsize()):
        print("reader从Queue获取到消息：%s"%q.get(True))
def writer(q):
    #print("writer启动(%s),⽗进程为(%s)"%(os.getpid(),os.getppid()))
    for i in "dongGe":
        q.put(i)
        print(i)
        time.sleep(1)
if __name__=="__main__":
    print("(%s) start"%os.getpid())
    q=Manager().Queue() #使⽤Manager中的Queue来初始化
    po=Pool()
    #使⽤阻塞模式创建进程，这样就不需要在reader中使⽤死循环了，可以让writer完全执⾏完成后，再⽤reader去读取
    po.apply(writer,(q,))
    po.apply(reader,(q,))
    po.close()
    po.join()
    print("(%s) End"%os.getpid())
