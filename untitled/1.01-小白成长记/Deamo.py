import threading
import time
import random
#共享变量
num =0
#创建对象
s = threading.Condition()
class scz(threading.Thread):
    def run(self):
        global num
        while True:
            if s.acquire():
                if num>10:
                    print('共享区已满，无法生产商品存入')
                else :
                    num +=3
                    sum =time.ctime()  + '生产了 1 件商品放入共享区, 共享区总计商品个数： ' + str(num)
                    print(sum)
                    s.notify()  # 唤醒其他阻塞状态的线程(如，消费者线程)
            s.release()  # 解除锁定
            time.sleep(1)

class xfz(threading.Thread):
    def run(self):
        global num  # 引用全局共享变量count
        while True:
            # 使用条件对象获取锁并锁定
            if s.acquire():
                # 判断共享变量是否已为0已空)
                if num < 1:
                    print ('共享区已空，消费者线程进入阻塞Block状态，停止获取！')
                    s.wait()  # 当前线程进入到阻塞状态
                else:
                    num -= 1  # 共享变量自件1
                    msg = time.ctime()  + '在共享区消费了1个商品,共享区总计商品个数为' + str(num)
                    print(msg)
                s.notify()

scz().start()
xfz().start()
