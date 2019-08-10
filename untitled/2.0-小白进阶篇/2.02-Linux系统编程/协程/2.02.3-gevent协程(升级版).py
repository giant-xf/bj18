# greenlet已经实现了协程，但是这个还的⼈⼯切换，是不是觉得太麻烦了，不
# 要捉急，python还有⼀个⽐greenlet更强⼤的并且能够⾃动切换任务的模
# 块 gevent
# 其原理是当⼀个greenlet遇到IO(指的是input output 输⼊输出，⽐如⽹络、⽂
# 件操作等)操作时，⽐如访问⽹络，就⾃动切换到其他的greenlet，等到IO操
# 作完成，再在适当的时候切换回来继续执⾏。
# 由于IO操作⾮常耗时，经常使程序处于等待状态，有了gevent为我们⾃动切
# 换协程，就保证总有greenlet在运⾏，⽽不是等待IO

#gevent自动识别耗时，遇到耗时操作自动转换另一个协程来运行
import gevent
def f(n):
    for i in range(n):
        print( gevent.getcurrent(), i)
        # ⽤来模拟⼀个耗时操作，注意不是time模块中的sleep
        gevent.sleep(1)
g1 = gevent.spawn(f, 5)
g2 = gevent.spawn(f, 5)
g3 = gevent.spawn(f, 5)
g1.join()
g2.join()
g3.join()
