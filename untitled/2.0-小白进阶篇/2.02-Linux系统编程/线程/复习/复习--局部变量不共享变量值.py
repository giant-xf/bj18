from threading import Thread
from time import sleep

class Mythreading(Thread):
    def __init__(self,num,sleeptime):
        Thread.__init__(self)
        self.num = num
        self.sleeptime = sleeptime

    def run(self):
        self.num +=1
        sleep(self.sleeptime)
        print("线程%s中num =%d"%(self.name,self.num))

if __name__ == '__main__':
    t1 = Mythreading(500,1)
    t2 = Mythreading(100,3)

    t1.start()
    t2.start()
