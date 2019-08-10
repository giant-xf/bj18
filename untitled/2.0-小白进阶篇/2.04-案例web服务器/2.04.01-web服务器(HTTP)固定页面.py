import socket
from multiprocessing import Process

from socket import *


def handleClient(client_socket):
    # 接受客户端发送过来的请求数据
    recvData = client_socket.recv(1024)
    #requestHeaderLines = recvData.splitlines()

    # 测试收到客户端发来的请求
    #print("recvData:",recvData)

    # 构造响应数据
    response_start_line = "HTTP/1.1 200 OK\r\n"
    response_headers = "server: My server\r\n"
    response_body = "hello Python"
    response = response_start_line+response_headers+"\r\n"+response_body

    # 向客户端发送返回数据
    client_socket.send(bytes(response,"utf-8"))
    #关闭客户端
    client_socket.close()

if __name__ == '__main__':
    # 创建服务器套接字
    server = socket(AF_INET,SOCK_STREAM)

    # 重复使用端口
    server.setsockopt(SOL_SOCKET, SO_REUSEADDR , 1)

    # 绑定IP 和 port
    server.bind(("",5201))

    # 最大允许连接个数
    server.listen(128)

    while True:
        # 创建一个客户端
        client_socket, client_address = server.accept()

        # 创建进程
        p =Process(target=handleClient,args=(client_socket,))
        # 启动进程
        p.start()
        # 关闭主进程套接字
        client_socket.close()



