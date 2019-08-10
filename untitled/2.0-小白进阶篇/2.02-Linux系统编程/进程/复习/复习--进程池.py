from multiprocessing import Pool

import time,os,random

def fu(num):
    for i in range(random.randint(1,6)):
        print("--%s开始运行---pid=%d"%(num,os.getpid()))
    time.sleep(1)

if __name__ == '__main__':
    po =Pool(3)

    for i in range(0,10):
        print("----%d----"%i)
        po.apply_async(fu,(i,))

    print("----start----")

    po.close()
    po.join()
    print("----over----")