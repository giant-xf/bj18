# 1. epoll的优点：
# 1. 没有最⼤并发连接的限制，能打开的FD(指的是⽂件描述符，通俗的理解
# 就是套接字对应的数字编号)的上限远⼤于1024
# 2. 效率提升，不是轮询的⽅式，不会随着FD数⽬的增加效率下降。只有活
# 跃可⽤的FD才会调⽤callback函数；即epoll最⼤的优点就在于它只管
# 你“活跃”的连接，⽽跟连接总数⽆关，因此在实际的⽹络环境中，epoll
# 的效率就会远远⾼于select和poll。

# 2. 说明
# EPOLLIN （可读）
# EPOLLOUT （可写）
# EPOLLET （ET模式）
# epoll对⽂件描述符的操作有两种模式：LT（level trigger）和ET（edge
# trigger）。LT模式是默认模式，LT模式与ET模式的区别如下：
# LT模式：当epoll检测到描述符事件发⽣并将此事件通知应⽤程序，应⽤程序可以不⽴即处理该事件。下次调⽤epoll时，会再次响应应⽤程序并通知此事件。
# ET模式：当epoll检测到描述符事件发⽣并将此事件通知应⽤程序，应⽤程序必须⽴即处理该事件

import  select
from socket import *
def main():
    #创建套接字
    s =socket(AF_INET,SOCK_STREAM)
    # 设置可以重复使⽤绑定的信息
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    # 绑定本机信息
    s.bind(("",5201))
    # 变为被动
    s.listen(10)

    # 创建⼀个epoll对象
    epoll=select.epoll()

    #s.fileno()表示对象 s 在操作系统中分配的文件描述符
    # 注册事件到epoll中
    # epoll.register(fd[, eventmask])
    # 注意，如果fd已经注册过，则会发⽣异常
    # 将创建的套接字添加到epoll的事件监听中
    epoll.register(s.fileno(),select.EPOLLIN|select.EPOLLET)

    connections = {}
    addresses = {}

    while True:
        # epoll 进⾏ fd 扫描的地⽅ -- 未指定超时时间则为阻塞等待
        epoll_list=epoll.poll()
        for fd,events in epoll_list:
            # print fd
            # print events
            # 如果是socket创建的套接字被激活
            if fd == s.fileno():
                conn,addr=s.accept()
                print('有新的客户端到来%s'%str(addr))
                # 将 conn 和 addr 信息分别保存起来
                connections[conn.fileno()] = conn
                addresses[conn.fileno()] = addr
                # 向 epoll 中注册 连接 socket 的 可读 事件
                epoll.register(conn.fileno(), select.EPOLLIN | select.EPOLLET)
            elif events == select.EPOLLIN:
                # 从激活 fd 上接收 
                #为什么用这个而不是用fd.recv ？
                #fd只表示一个数值，而不是对象，前面使用字典将clientSoket对象
                #放进去了，
                recvData = connections[fd].recv(1024)
                if len(recvData)>0:
                    print('recv:%s'%recvData.decode("gb2312"))
                else:
                    # 从 epoll 中移除该 连接 fd
                    epoll.unregister(fd)
                    # server 侧主动关闭该 连接 fd
                    #为什么还要使用epoll.unregister ?
                    #关闭这个还是不够的，只关闭了这个调用出来的clientSocket
                    #然而在epoll中注册的还没有删除，那样程序重新来一遍的时候还
                    #会继续调用，并没有完全关闭
                    connections[fd].close()
                    print("%s---offline---"%str(addresses[fd]))        






if __name__ == '__main__':
    main()

