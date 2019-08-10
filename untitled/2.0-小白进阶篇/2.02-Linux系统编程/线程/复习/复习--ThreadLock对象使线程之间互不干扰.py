# 在多线程环境下，每个线程都有⾃⼰的数据。⼀个线程使⽤⾃⼰的局部变量
# ⽐使⽤全局变量好，因为局部变量只有线程⾃⼰能看⻅，不会影响其他线
# 程，⽽全局变量的修改必须加锁。

import threading

# 创建全局ThreadLocal对象:
local_school = threading.local()
def process_student():
# 获取当前线程关联的student:
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))
def process_thread(name):
# 绑定ThreadLocal的student:
    local_school.student = name
    process_student()

if __name__ == '__main__':

    t1 = threading.Thread(target= process_thread, args=('dongGe',), name=())
    t2 = threading.Thread(target= process_thread, args=('⽼王',), name=())
    t1.start()
    t2.start()
    t1.join()
    t2.join()
