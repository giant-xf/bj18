# -*- coding:utf-8 -*-
from socket import *
import struct,os

def main():
    #1.获取需要下载的文件名
    filename =input("请输入要下载的文件名:")

    #2.创建套接字
    udpSocket =socket(AF_INET, SOCK_DGRAM)
        #网络传输中的语句
    sendDate = struct.pack("!H%dsb5sb" %len(filename), 1, filename, 0, "octet", 0)
    #3.发送数据请求               元组
    udpSocket.sendto(sendDate,("192.168.246.1",69))

    flag =True
    num =0
    f =open(filename,"w")
    while True:
        # 3. 接收服务发送回来的应答数据
        recv =udpSocket.recvfrom(1024)
        #前者是操作码和块编码
        #后者是发送方的IP和端口
        recvDate, serverDate =recv
        #操作码
        opNum =struct.unpack("!H",recvDate[:2])
        #块编码                        返回的是元组
        printNum =struct.unpack("!H",recvDate[2:4])

        if opNum[0] ==3:
            num +=1

            if num ==2**16:
                num =0

            if num ==printNum[0]:
                f.write(recvDate[4:])
                num =printNum[0]
            #整理ACK的数据包      操作码 和 块编码
            ackDate =struct.pack("!HH",4,printNum[0])
            udpSocket.sendto(ackDate,serverDate)

        elif  opNum[0] ==5:
            print("文件名错误或没有此文件....")
            flag =False

        if len(recv) < 516:
            break

    if flag ==True:
        f.close()

    else:
        os.unlink(filename)  # 如果没有要下载的文件，那么就需要把刚刚创建的文件进行删除

if __name__ == '__main__':
    main()


