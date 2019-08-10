from multiprocessing import Process

import os

class NewMyProcess(Process):
    #单例模式
    # count =None
    # count_flag =True
    #
    # def __new__(cls, *args, **kwargs):
    #     if cls.count == None :
    #         cls.count = object.__new__(cls)
    #         return cls.count
    #     else:
    #         return cls.count
    #
    # def __init__(self,name):
    #
    #     Process.__init__(self)
    #
    #     if self.count_flag:
    #         self.name = name
    #         self.count_flag =False


    def run(self):
        print("----子进程在运行---name=%s-----pid=%d--ppid=%d"%(self.name,os.getpid(),os.getppid()))

if __name__ == '__main__':
    p =NewMyProcess()
    p1 = NewMyProcess()
    p.start()
    p1.start()
    p.join()
    print("-----主进程在运行----%d"%os.getpid())


