import threading,time

class MyThread(threading.Thread):
    def __init__(self,name):

        #重写__init__() 方法
        threading.Thread.__init__(self)
        self.name = name

    def run(self):
        for i in range(3):
            time.sleep(1)
            msg ="I'm"+"---"+self.name+"---"+"@"+str(i)
            print(msg)

def test():
    for i in range(5):
        t1 = MyThread(i)
        t1.start()



if __name__ == '__main__':
    test()