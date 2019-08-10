from greenlet import greenlet
import time
def A():
    while True:
        print ("---A--")
        gr2.switch()
        time.sleep(0.5)
def B():
    while True:
        print ("---B--")
        gr1.switch()
        time.sleep(0.5)
gr1 = greenlet(A)
gr2 = greenlet(B)
#切换到gr1中运⾏
gr1.switch()
