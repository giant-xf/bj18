from threading import Thread,Lock

num = 100

def work1():
    global num

    for i in range(1000000):
        mutex.acquire()   #尽量让关键位置上锁，上锁部分少效率块
        num +=1
        mutex.release()
    print("work1 num=%d"%num)

def work2():
    global num

    for i in range(1000000):
        mutex.acquire()
        num +=1
        mutex.release()
    print("work2 num=%d"%num)

if __name__ == '__main__':
    mutex= Lock()

    t1 = Thread(target=work1)
    t2 = Thread(target=work2)

    t1.start()
    t2.start()

    print(num)