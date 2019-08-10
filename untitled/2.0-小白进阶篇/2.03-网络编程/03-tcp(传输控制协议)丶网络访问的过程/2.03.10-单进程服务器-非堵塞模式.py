from socket import *

def main():
    serSocket = socket(AF_INET, SOCK_STREAM)
    # 重复使⽤绑定的信息
    serSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR , 1)
    localAddr = ('', 5201)
    serSocket.bind(localAddr)
    #将套接字设置为⾮堵塞
    #设置为⾮堵塞后，如果accept时，恰巧没有客户端connect，那么accept会
    #产⽣⼀个异常，所以需要try来进⾏处理
    serSocket.setblocking(False)
    serSocket.listen(5)
    clientlist =[]
    flag =True
    while True:
        try:
            #等待一个新客户端到来
            clientSocket,clientAddr = serSocket.accept()
            clientSocket.setblocking(False)
            clientlist.append((clientSocket,clientAddr))
            flag =False
        except:
            pass
        else:
            print("一个新客户端加入:%s,当前客户端数为%d"%(str(clientAddr),len(clientlist)))
            
        if len(clientlist)!=0:
            for clientSocket,clientAddr in clientlist:
                try:
                    recvDate =clientSocket.recv(1024)
                except:
                    pass
                else:
                    if len(recvDate)>1:
                        print("[%s]:%s"%(str(clientAddr),recvDate.decode("gb2312")))
                    else:
                        print("客户端%s下线了,当前客户端数为%d"%(str(clientAddr),len(clientlist)-1))
                        clientSocket.close()
                        clientlist.remove((clientSocket,clientAddr))
        elif len(clientlist)==0 and flag ==False:
            print("当前连接的客户端为0，服务器下线")
            serSocket.close()
            break




if __name__ == '__main__':
    main()
