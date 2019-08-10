from socket import *



# 如果想要完成⼀个tcp服务器的功能，需要的流程如下：
# 1. socket创建⼀个套接字
# 2. bind绑定ip和port
# 3. listen使套接字变为可以被动链接
# 4. accept等待客户端的链接
# 5. recv/send接收发送数据


# 1. socket创建⼀个套接字
serverSocket = socket(AF_INET, SOCK_STREAM)
# 2. bind绑定ip和port
serverSocket.bind(("", 5201))
# 3. listen使套接字变为可以被动链接
serverSocket.listen(5)

print("-----1-----")    #执行程序后会打印第一步
# 4. accept等待客户端的链接
clientSocket,clientInfo = serverSocket.accept()
#clientSocket 表示这个新的客户端（相当于新的套接字）
#clientInfo 表示这个新的客户端的ip以及port
print("-----2-----")    #当有客户端连接到服务器是就会打印第二步
serverSocket.sendto("您成功连接到了服务器！！".encode("gb2312"),clientInfo)

# 5. recv/send接收发送数据
recvData = clientSocket.recv(1024)

print("-----3-----")       #当接受到客户端发送的消息时会打印第三步
print("%s:%s"%(str(clientInfo), recvData))

clientSocket.close()
serverSocket.close()


#创建一个TCP客户端
# 1. socket创建⼀个套接字
clientSocket = socket(AF_INET, SOCK_STREAM)
# 2. 连接服务器
clientSocket.connect(("192.168.119.153", 8989))

#注意：
# 1. tcp客户端已经链接好了服务器，所以在以后的数据发送中，不需要填写对方的iph和port----->打电话
# 2. udp在发送数据的时候，因为没有之前的链接，所依需要　在每次的发送中　都要填写接收方的ip和port－－－－－＞写信　
#发送数据
clientSocket.send("haha".encode("gb2312"))
#接收数据
recvData = clientSocket.recv(1024)

print("recvData:%s"%recvData)

clientSocket.close()

