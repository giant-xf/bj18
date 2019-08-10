#coding='utf-8'
from socket import *
from multiprocessing import  *
from threading import Thread


def dealWithClient(clientSocket,destAddr):
    while True:
        recvDate =clientSocket.recv(1024)
        if len(recvDate)>0:
            print('recv[%s]:%s'%(str(destAddr), recvDate.decode("gb2312")))
        else:
            print('[%s]客户端已经关闭'%str(destAddr))
            break
    clientSocket.close()
def main():

    serSocket = socket(AF_INET, SOCK_STREAM)
    # 重复使⽤绑定的信息
    serSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR , 1)
    localAddr = ('', 5201)
    serSocket.bind(localAddr)
    serSocket.listen(5)
    try:
        print('-----主进程，，等待新客户端的到来------') 
        while True:
            
            clientSocket,destAddr =serSocket.accept()
            print('-----主进程，，接下来负责数据处理[%s]-----'%str(destAddr))
            #setblocking(False)
            client =Process(target=dealWithClient,args=(clientSocket,destAddr))
            client.start()
            #因为已经向⼦进程中copy了⼀份（引⽤），并且父线程和子线程共用一份数据
            #clientSocket.close()
    finally:
        #当为所有的客户端服务完之后再进⾏关闭，表示不再接收新的客户端的链接
        serSocket.close()

if __name__ == '__main__':
    main()

        
