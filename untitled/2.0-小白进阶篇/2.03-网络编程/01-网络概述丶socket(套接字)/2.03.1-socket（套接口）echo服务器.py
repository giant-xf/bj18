from socket import *

up =socket(AF_INET,SOCK_DGRAM)

#发送数据接收方的IP以及端口号
sendAddr =('192.168.246.1',6666)
#sendDate =input('请输入要发送的信息:')

#绑定自己的端口号，IP一般不用填写
bindAddr =('',5203)
up.bind(bindAddr)

#发送数据
up.sendto(b'hello',sendAddr)

#每次接收数据的字节数大小
recv =up.recvfrom(1024)
#打印接收到的数据
print(recv)

#关闭socket
up.close()