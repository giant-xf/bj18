#coding=utf-8
from socket import *
from threading import Thread

udpSocket =socket(AF_INET, SOCK_DGRAM)
destIP =''
destPort=0

#创建接收函数
def SocketInfo():
#每次接收数据的字节数大小
	while True:
		recv =udpSocket.recvfrom(1024)
#打印接收到的数据
		print("\r\r>>[%s]%s\n<<"%(str(recv[1]),recv[0].decode("gb18030")),end='')

#创建发送函数	
def SocketOut():
#发送数据
	while True:
		sendDate=input("<<")
		udpSocket.sendto(sendDate.encode("gb2312"), (destIP, destPort))

def main():
	
	global destIP 
	global destPort

#发送数据接收方的IP以及端口号
#	sendDate =input('请输入要发送的信息:')
#自己输入目标的IP和端口
	destIP=input("请输入目标的IP:")
	destPort=int(input("请输入目标的Port:"))
#绑定自己的端口号，IP一般不用填写
	bindAddr =('',5201)
	udpSocket.bind(bindAddr)

	tI =Thread(target =SocketInfo)
	tO =Thread(target =SocketOut)
	tI.start()
	tO.start()

#阻塞主进程
	tI.join()
	tO.join()



#关闭socket
#	upSocket.close()

if __name__=="__main__":
	main()
