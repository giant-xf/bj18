from threading import Thread

from time import sleep

list = [1,2,3]

def work1():
    for i in "work":
        list.append(i)

def work2():
    sleep(3)
    print("work2  is list :"+str(list))

if __name__ == '__main__':
    t1 = Thread(target=work1)
    t2 = Thread(target=work2)

    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(list)