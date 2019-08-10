#coding =utf-8
import os,struct
from  socket import *

def main():
    #1.接受要传输的文件名
    filename =input("请输入要上传的文件名:")

    #2.创建套接字
    udpSocket = socket(AF_INET, SOCK_DGRAM)

    #3.发送请求信号
        #  网络传输中的语句(数据打包)
    sendDate = struct.pack("!H%dsb5sb" % len(filename), 2, filename, 0, "octet", 0)
    udpSocket.sendto(sendDate, ("192.168.246.1", 69))

    #4.绑定端口
    #udpSocket.bind("",5201)




if __name__ == '__main__':
    main()