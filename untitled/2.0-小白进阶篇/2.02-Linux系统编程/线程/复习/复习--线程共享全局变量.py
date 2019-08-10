import threading,time

num = 100

def work1():
    global num

    for i in range(3):
        num +=1
    print("work1 中num的值为:%d"%num)
def work2():
    global num

    print("work2 中num 的值为:%d"%num)

if __name__ == '__main__':
    t1 = threading.Thread(target=work1)
    t2 = threading.Thread(target=work2)

    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("全局变量中的num的值为:%d"%num)