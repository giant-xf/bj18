import select
from socket import *
import sys
def main():
    #创建套接字的步骤不变
    server = socket(AF_INET, SOCK_STREAM)
    server.setsockopt(SOL_SOCKET, SO_REUSEADDR , 1)
    server.bind(('', 5201))
    server.listen(11)

    # 监听到键盘
    inputs =[server, sys.stdin]
    running =True

    while True:
        # 调⽤ select 函数，阻塞等待                 #三种状态
        readable, writeable, exceptional = select.select(inputs, [], [])
        # 数据抵达，循环
        for sock in readable:
            # 监听到有新的连接
            if sock == server:
                conn, addr = server.accept()
                print("有新的客户端加入!%s"%str(addr))
                # select 监听的socket
                inputs.append(conn)
            # 监听到键盘有输⼊
            elif sock == sys.stdin:
                cmd = sys.stdin.readline()
                running = False
                break
            # 有数据到达
            else:
                # 读取客户端连接发送的数据
                data = sock.recv(1024)
                if data:
                    print("%s:%s"%(str(addr),data.decode("gb2312")))
                    sock.send(data)
                else:
                    print("%s已下线"%str(addr))
                    # 移除select监听的socket
                    inputs.remove(sock)
                    sock.close()
        # 如果检测到⽤户输⼊敲击键盘，那么就退出
        if not running:
            break  
    server.close()

if __name__ == '__main__':
    main()



