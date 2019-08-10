# 同步调⽤: 比如我借给你一本书，你说下次星期一还给我，我就一直在这里等等等，白等
# 异步调⽤: 就是我借你一本书，你说下次还给我的时候和我说一声，我去干自己的事情，
#           你还给我的时候我来接受，然后继续干别的事(效率高)

#子进程做自己的事情，主进程做自己自己的事，不知道什么时候做完，然而操作系统
#   突然调用主进程，主进程做完了这件事以后继续做自己的事
from multiprocessing import Pool
import time
import os
def work1():
    print("---进程池中的进程---pid=%d,ppid=%d--"%(os.getpid(),os.getppid()))
    for i in range(3):
        print("----%d---"%i)
        time.sleep(1)
    return "hahah"

def work2(args):
    print("---callback func--pid=%d"%os.getpid())
    print("---callback func--args=%s"%args)

if __name__ == '__main__':
    pool = Pool(3)                 #回调,可以的到子线程返回的值，由主线程来完成
    pool.apply_async(func=work1,callback=work2)
    while True:
        time.sleep(1)
        print("----主进程-pid=%d----"%os.getpid())
